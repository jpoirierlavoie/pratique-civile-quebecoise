#!/usr/bin/env python3
"""Inspecteur local des métadonnées et structures cachées des pièces (.docx, .xlsx, .eml, .pdf, images).

Bibliothèque standard Python uniquement, lecture seule, aucun appel réseau.
Usage : python scripts/inspecter_piece.py <fichier>... [--json]
"""

from __future__ import annotations

import argparse
from email import policy
from email.parser import BytesParser
import hashlib
import json
import mimetypes
from pathlib import Path
import re
import struct
import sys
import xml.etree.ElementTree as ET
import zipfile
import zlib

_DOCX_EXTS = {".docx", ".docm"}
_XLSX_EXTS = {".xlsx", ".xlsm"}
_EML_EXTS = {".eml"}
_PDF_EXTS = {".pdf"}
_JPEG_EXTS = {".jpg", ".jpeg"}
_PNG_EXTS = {".png"}

_W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
_DC_NS = "http://purl.org/dc/elements/1.1/"
_CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
_DCTERMS_NS = "http://purl.org/dc/terms/"
_APP_NS = "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
_MAIN_SS_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
_REL_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

_PDF_HEADER_RE = re.compile(rb"%PDF-(\d+\.\d+)")
_PDF_PAGE_RE = re.compile(rb"/Type\s*/Page(?![A-Za-z])")
_PDF_ENCRYPT_RE = re.compile(rb"/Encrypt\b")
_PDF_ANNOTS_RE = re.compile(rb"/Annots\b")
_PDF_ACROFORM_RE = re.compile(rb"/AcroForm\b")
_PDF_SIG_RE = re.compile(rb"/Type\s*/Sig\b|/FT\s*/Sig\b")
_PDF_STREAM_RE = re.compile(rb"stream\r?\n(.*?)\r?\nendstream", re.S)
_PDF_TEXT_OP_RE = re.compile(rb"\bBT\b.*?(?:\bTj\b|\bTJ\b)", re.S)


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconf = getattr(stream, "reconfigure", None)
        if callable(reconf):
            reconf(encoding="utf-8", errors="replace")


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _truncate(text: str, limit: int = 120) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= limit:
        return cleaned
    return cleaned[: limit - 1] + "…"


def _parse_xml_from_zip(zf: zipfile.ZipFile, member: str) -> ET.Element | None:
    try:
        data = zf.read(member)
    except KeyError:
        return None
    return ET.fromstring(data)


def _extract_ooxml_props(zf: zipfile.ZipFile) -> dict[str, str]:
    props: dict[str, str] = {}
    core = _parse_xml_from_zip(zf, "docProps/core.xml")
    if core is not None:
        mapping = {
            f"{{{_DC_NS}}}creator": "auteur_initial",
            f"{{{_CP_NS}}}lastModifiedBy": "dernier_editeur",
            f"{{{_DCTERMS_NS}}}created": "date_creation",
            f"{{{_DCTERMS_NS}}}modified": "date_modification",
            f"{{{_DC_NS}}}title": "titre",
            f"{{{_DC_NS}}}subject": "objet",
            f"{{{_CP_NS}}}revision": "revision",
        }
        for tag, label in mapping.items():
            el = core.find(tag)
            if el is not None and el.text and el.text.strip():
                props[label] = el.text.strip()

    app = _parse_xml_from_zip(zf, "docProps/app.xml")
    if app is not None:
        app_map = {
            f"{{{_APP_NS}}}Application": "application",
            f"{{{_APP_NS}}}Company": "organisation",
            f"{{{_APP_NS}}}TotalTime": "temps_edition_min",
            f"{{{_APP_NS}}}Pages": "pages_declarees",
            f"{{{_APP_NS}}}Words": "mots_declares",
        }
        for tag, label in app_map.items():
            el = app.find(tag)
            if el is not None and el.text and el.text.strip():
                props[label] = el.text.strip()
    return props


def _inspect_docx(path: Path) -> dict[str, object]:
    indicateurs: list[str] = []
    details: dict[str, object] = {}

    try:
        zf_ctx = zipfile.ZipFile(path, "r")
    except zipfile.BadZipFile:
        return {
            "statut": "erreur",
            "erreur": "Archive OOXML invalide ou corrompue (.docx).",
        }

    with zf_ctx as zf:
        details["proprietes"] = _extract_ooxml_props(zf)

        comments_root = _parse_xml_from_zip(zf, "word/comments.xml")
        commentaires: list[dict[str, str]] = []
        if comments_root is not None:
            for com in comments_root.findall(f".//{{{_W_NS}}}comment"):
                author = com.attrib.get(f"{{{_W_NS}}}author", "")
                date = com.attrib.get(f"{{{_W_NS}}}date", "")
                texte = "".join(com.itertext()).strip()
                commentaires.append(
                    {
                        "auteur": author,
                        "date": date,
                        "extrait": _truncate(texte),
                    }
                )
        details["nombre_commentaires"] = len(commentaires)
        if commentaires:
            indicateurs.append("COMMENTAIRES_WORD")
            details["commentaires_apercu"] = commentaires[:15]

        insertions = 0
        suppressions = 0
        rev_authors: set[str] = set()
        xml_targets = [
            name
            for name in zf.namelist()
            if name == "word/document.xml"
            or (name.startswith("word/header") and name.endswith(".xml"))
            or (name.startswith("word/footer") and name.endswith(".xml"))
        ]
        for member in xml_targets:
            root = _parse_xml_from_zip(zf, member)
            if root is None:
                continue
            for tag_local, counter_kind in (("ins", "ins"), ("del", "del")):
                for node in root.findall(f".//{{{_W_NS}}}{tag_local}"):
                    if counter_kind == "ins":
                        insertions += 1
                    else:
                        suppressions += 1
                    author = node.attrib.get(f"{{{_W_NS}}}author")
                    if author:
                        rev_authors.add(author)

        details["marques_revision"] = {
            "insertions": insertions,
            "suppressions": suppressions,
            "auteurs": sorted(rev_authors),
        }
        if insertions or suppressions:
            indicateurs.append("MARQUES_DE_REVISION")

        rels_root = _parse_xml_from_zip(zf, "word/_rels/settings.xml.rels")
        attached_templates: list[str] = []
        if rels_root is not None:
            for rel in rels_root:
                rel_type = rel.attrib.get("Type", "")
                if rel_type.endswith("/attachedTemplate"):
                    target = rel.attrib.get("Target", "")
                    if target:
                        attached_templates.append(target)
        if attached_templates:
            indicateurs.append("MODELE_ATTACHE")
            details["modeles_attaches"] = attached_templates

    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": details,
    }


def _inspect_xlsx(path: Path) -> dict[str, object]:
    indicateurs: list[str] = []
    details: dict[str, object] = {}

    try:
        zf_ctx = zipfile.ZipFile(path, "r")
    except zipfile.BadZipFile:
        return {
            "statut": "erreur",
            "erreur": "Archive OOXML invalide ou corrompue (.xlsx).",
        }

    with zf_ctx as zf:
        details["proprietes"] = _extract_ooxml_props(zf)

        wb_root = _parse_xml_from_zip(zf, "xl/workbook.xml")
        rels_root = _parse_xml_from_zip(zf, "xl/_rels/workbook.xml.rels")
        rel_targets: dict[str, str] = {}
        if rels_root is not None:
            for rel in rels_root:
                rid = rel.attrib.get("Id")
                target = rel.attrib.get("Target", "")
                if rid:
                    norm = target.lstrip("/")
                    if not norm.startswith("xl/"):
                        norm = f"xl/{norm}"
                    rel_targets[rid] = norm

        feuilles: list[dict[str, str]] = []
        target_to_sheet: dict[str, str] = {}
        has_hidden = False
        if wb_root is not None:
            for sheet in wb_root.findall(f".//{{{_MAIN_SS_NS}}}sheet"):
                name = sheet.attrib.get("name", "")
                state = sheet.attrib.get("state", "visible")
                rid = sheet.attrib.get(f"{{{_REL_NS}}}id", "")
                if state != "visible":
                    has_hidden = True
                feuilles.append({"nom": name, "etat": state})
                if rid in rel_targets:
                    target_to_sheet[rel_targets[rid]] = name

        details["feuilles"] = feuilles
        if has_hidden:
            indicateurs.append("FEUILLES_CACHEES")

        sheet_members = sorted(
            name
            for name in zf.namelist()
            if name.startswith("xl/worksheets/") and name.endswith(".xml")
        )
        formula_count = 0
        formula_samples: list[dict[str, str]] = []
        cell_count = 0
        for member in sheet_members:
            ws_root = _parse_xml_from_zip(zf, member)
            if ws_root is None:
                continue
            sheet_label = target_to_sheet.get(member, Path(member).stem)
            for cell in ws_root.findall(f".//{{{_MAIN_SS_NS}}}c"):
                cell_count += 1
                f_el = cell.find(f"{{{_MAIN_SS_NS}}}f")
                if f_el is not None:
                    formula_count += 1
                    if len(formula_samples) < 15:
                        ref = cell.attrib.get("r", "?")
                        expr = f_el.text or "(formule partagée ou matricielle)"
                        formula_samples.append(
                            {
                                "cellule": f"{sheet_label}!{ref}",
                                "formule": _truncate(f"={expr}", 100),
                            }
                        )

        details["nombre_cellules"] = cell_count
        details["nombre_formules"] = formula_count
        if formula_samples:
            details["echantillon_formules"] = formula_samples
        if formula_count > 0:
            indicateurs.append("FORMULES_PRESENTES")

        ext_links: list[str] = []
        for name in zf.namelist():
            if name.startswith("xl/externalLinks/_rels/") and name.endswith(".rels"):
                ext_root = _parse_xml_from_zip(zf, name)
                if ext_root is not None:
                    for rel in ext_root:
                        target = rel.attrib.get("Target")
                        if target:
                            ext_links.append(target)
        details["liens_externes"] = ext_links
        if ext_links:
            indicateurs.append("LIENS_EXTERNES")

        comment_files = [
            name
            for name in zf.namelist()
            if (name.startswith("xl/comments") or name.startswith("xl/threadedComments/"))
            and name.endswith(".xml")
        ]
        comment_count = 0
        for member in comment_files:
            c_root = _parse_xml_from_zip(zf, member)
            if c_root is None:
                continue
            comment_count += len(c_root.findall(f".//{{{_MAIN_SS_NS}}}comment"))
            comment_count += len(
                [el for el in c_root.iter() if el.tag.endswith("}threadedComment")]
            )
        details["nombre_commentaires"] = comment_count
        if comment_count > 0:
            indicateurs.append("COMMENTAIRES_TABLEUR")

    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": details,
    }


def _inspect_eml(path: Path) -> dict[str, object]:
    indicateurs: list[str] = []
    raw = path.read_bytes()
    msg = BytesParser(policy=policy.default).parsebytes(raw)

    headers_keys = (
        "From",
        "To",
        "Cc",
        "Bcc",
        "Reply-To",
        "Date",
        "Subject",
        "Message-ID",
        "In-Reply-To",
        "References",
        "X-Unsent",
    )
    en_tetes: dict[str, str] = {}
    for key in headers_keys:
        val = msg.get(key)
        if val is not None:
            en_tetes[key] = _truncate(str(val), 200)

    received_headers = msg.get_all("Received") or []
    received_count = len(received_headers)

    if en_tetes.get("X-Unsent") == "1" or (
        received_count == 0 and not en_tetes.get("Message-ID")
    ):
        indicateurs.append("BROUILLON_PROBABLE")
    if en_tetes.get("Bcc"):
        indicateurs.append("COPIE_CONFORME_INVISIBLE")
    if en_tetes.get("In-Reply-To") or en_tetes.get("References"):
        indicateurs.append("COURRIEL_DANS_CHAINE")
    if (
        en_tetes.get("Reply-To")
        and en_tetes.get("From")
        and en_tetes["Reply-To"].lower() != en_tetes["From"].lower()
    ):
        indicateurs.append("ADRESSE_REPONSE_DIFFERENTE")

    pieces_jointes: list[dict[str, object]] = []
    for part in msg.walk():
        if part.is_multipart():
            continue
        disp = part.get_content_disposition()
        filename = part.get_filename()
        ctype = part.get_content_type()
        if filename or disp == "attachment" or (
            ctype not in ("text/plain", "text/html") and disp is not None
        ):
            payload = part.get_payload(decode=True)
            size = len(payload) if payload is not None else 0
            pieces_jointes.append(
                {
                    "nom": filename or "(sans nom)",
                    "type_mime": ctype,
                    "disposition": disp or "",
                    "taille_octets": size,
                }
            )

    if pieces_jointes:
        indicateurs.append("PIECES_JOINTES_PRESENTES")

    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": {
            "en_tetes": en_tetes,
            "nombre_relais_received": received_count,
            "pieces_jointes": pieces_jointes,
        },
    }


def _decode_pdf_bytes(raw_val: bytes) -> str:
    if raw_val.startswith(b"\xfe\xff"):
        return raw_val[2:].decode("utf-16-be", errors="replace").strip("\x00")
    if raw_val.startswith(b"\xff\xfe"):
        return raw_val[2:].decode("utf-16-le", errors="replace").strip("\x00")
    return raw_val.decode("latin-1", errors="replace").strip("\x00")


def _extract_pdf_literal(blob: bytes, key: bytes) -> str | None:
    pattern = re.compile(
        b"/"
        + re.escape(key)
        + rb"\s*(?:\(((?:\\.|[^\\()])*)\)|<([0-9A-Fa-f\s]+)>)"
    )
    m = pattern.search(blob)
    if not m:
        return None
    if m.group(1) is not None:
        raw = m.group(1)
        unescaped = re.sub(
            rb"\\([\\()nrtbf])",
            lambda hit: {
                b"\\": b"\\",
                b"(": b"(",
                b")": b")",
                b"n": b"\n",
                b"r": b"\r",
                b"t": b"\t",
                b"b": b"\b",
                b"f": b"\f",
            }[hit.group(1)],
            raw,
        )
        return _truncate(_decode_pdf_bytes(unescaped), 200)
    hex_str = re.sub(rb"\s+", b"", m.group(2))
    if len(hex_str) % 2 == 1:
        hex_str += b"0"
    try:
        return _truncate(_decode_pdf_bytes(bytes.fromhex(hex_str.decode("ascii"))), 200)
    except ValueError:
        return None


def _try_optional_pdf_lib(path: Path) -> dict[str, object] | None:
    try:
        import pypdf  # type: ignore[import-not-found]
    except ImportError:
        pypdf = None

    if pypdf is not None:
        try:
            reader = pypdf.PdfReader(str(path))
            encrypted = bool(getattr(reader, "is_encrypted", False))
            meta_raw = {} if encrypted else (reader.metadata or {})
            meta = {
                k.lstrip("/"): _truncate(str(v), 200)
                for k, v in meta_raw.items()
                if v is not None and str(v).strip()
            }
            if encrypted:
                return {
                    "analyseur": "pypdf",
                    "chiffre": True,
                    "nombre_pages": None,
                    "pages_sans_texte": [],
                    "couche_texte": "chiffree",
                    "metadonnees": meta,
                    "annotations": None,
                    "formulaire": None,
                    "signatures": None,
                }
            empty_pages: list[int] = []
            has_annots = False
            for idx, page in enumerate(reader.pages, start=1):
                txt = (page.extract_text() or "").strip()
                if not txt:
                    empty_pages.append(idx)
                if "/Annots" in page:
                    has_annots = True
            total_pages = len(reader.pages)
            couche = (
                "absente"
                if total_pages > 0 and len(empty_pages) == total_pages
                else ("partielle" if empty_pages else "detectee")
            )
            root_obj = reader.trailer.get("/Root", {})
            has_acro = False
            has_sig = False
            try:
                resolved_root = root_obj.get_object() if hasattr(root_obj, "get_object") else root_obj
                has_acro = "/AcroForm" in resolved_root
                if has_acro:
                    acro = resolved_root["/AcroForm"].get_object()
                    has_sig = "/SigFlags" in acro
            except Exception:
                pass
            return {
                "analyseur": "pypdf",
                "chiffre": False,
                "nombre_pages": total_pages,
                "pages_sans_texte": empty_pages,
                "couche_texte": couche,
                "metadonnees": meta,
                "annotations": has_annots,
                "formulaire": has_acro,
                "signatures": has_sig,
            }
        except Exception:
            return None

    return None


def _inspect_pdf(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    header_m = _PDF_HEADER_RE.search(raw[:1024])
    version = header_m.group(1).decode("ascii") if header_m else "inconnue"

    indicateurs: list[str] = []
    lib_res = _try_optional_pdf_lib(path)

    if lib_res is not None:
        lib_res["version_pdf"] = version
        if lib_res.get("chiffre"):
            indicateurs.append("PDF_CHIFFRE")
        elif lib_res.get("couche_texte") == "absente":
            indicateurs.append("AUCUNE_COUCHE_TEXTE_DETECTEE")
        elif lib_res.get("couche_texte") == "partielle":
            indicateurs.append("COUCHE_TEXTE_PARTIELLE")
        if lib_res.get("annotations"):
            indicateurs.append("ANNOTATIONS_PRESENTES")
        if lib_res.get("formulaire"):
            indicateurs.append("FORMULAIRE_ACROFORM")
        if lib_res.get("signatures"):
            indicateurs.append("SIGNATURE_ELECTRONIQUE_DETECTEE")
        return {
            "statut": "ok",
            "indicateurs": indicateurs,
            "details": lib_res,
        }

    encrypted = bool(_PDF_ENCRYPT_RE.search(raw))
    pages = len(_PDF_PAGE_RE.findall(raw))
    has_annots = bool(_PDF_ANNOTS_RE.search(raw))
    has_acro = bool(_PDF_ACROFORM_RE.search(raw))
    has_sig = bool(_PDF_SIG_RE.search(raw))

    meta: dict[str, str] = {}
    for pdf_key, label in (
        (b"Title", "Title"),
        (b"Author", "Author"),
        (b"Creator", "Creator"),
        (b"Producer", "Producer"),
        (b"CreationDate", "CreationDate"),
        (b"ModDate", "ModDate"),
    ):
        val = _extract_pdf_literal(raw, pdf_key)
        if val:
            meta[label] = val

    text_stream_hits = 0
    if not encrypted:
        for m in _PDF_STREAM_RE.finditer(raw):
            chunk = m.group(1)
            if len(chunk) > 8_000_000:
                continue
            candidates = [chunk]
            try:
                candidates.append(zlib.decompress(chunk))
            except zlib.error:
                pass
            for cand in candidates:
                if _PDF_TEXT_OP_RE.search(cand):
                    text_stream_hits += 1
                    break

    if encrypted:
        couche = "chiffree"
        indicateurs.append("PDF_CHIFFRE")
    elif text_stream_hits == 0:
        couche = "absente"
        indicateurs.append("AUCUNE_COUCHE_TEXTE_DETECTEE")
    else:
        couche = "detectee"

    if has_annots:
        indicateurs.append("ANNOTATIONS_PRESENTES")
    if has_acro:
        indicateurs.append("FORMULAIRE_ACROFORM")
    if has_sig:
        indicateurs.append("SIGNATURE_ELECTRONIQUE_DETECTEE")

    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": {
            "analyseur": "stdlib-binaire",
            "version_pdf": version,
            "chiffre": encrypted,
            "nombre_pages_estime": pages,
            "flux_texte_detectes": text_stream_hits,
            "couche_texte": couche,
            "metadonnees": meta,
            "annotations": has_annots,
            "formulaire": has_acro,
            "signatures": has_sig,
        },
    }


def _read_u16(buf: bytes, offset: int, endian: str) -> int:
    return struct.unpack_from(f"{endian}H", buf, offset)[0]


def _read_u32(buf: bytes, offset: int, endian: str) -> int:
    return struct.unpack_from(f"{endian}I", buf, offset)[0]


def _parse_ifd(
    tiff: bytes, offset: int, endian: str, tag_map: dict[int, str]
) -> tuple[dict[str, str], int | None]:
    result: dict[str, str] = {}
    exif_ifd_offset: int | None = None
    if offset + 2 > len(tiff):
        return result, None
    count = _read_u16(tiff, offset, endian)
    pos = offset + 2
    for _ in range(count):
        if pos + 12 > len(tiff):
            break
        tag = _read_u16(tiff, pos, endian)
        typ = _read_u16(tiff, pos + 2, endian)
        num = _read_u32(tiff, pos + 4, endian)
        val_field = tiff[pos + 8 : pos + 12]
        val_offset = _read_u32(tiff, pos + 8, endian)
        pos += 12

        if tag == 0x8769:
            exif_ifd_offset = val_offset
            continue
        if tag == 0x8825:
            result["GPSInfo_present"] = "oui"
            continue
        if tag in tag_map and typ == 2 and num > 0:
            if num <= 4:
                raw_bytes = val_field[:num]
            elif val_offset + num <= len(tiff):
                raw_bytes = tiff[val_offset : val_offset + num]
            else:
                continue
            decoded = raw_bytes.rstrip(b"\x00").decode("utf-8", errors="replace").strip()
            if decoded:
                result[tag_map[tag]] = _truncate(decoded, 120)
    return result, exif_ifd_offset


def _inspect_jpeg(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    exif_tags: dict[str, str] = {}
    pos = 2
    if data.startswith(b"\xff\xd8"):
        while pos + 4 <= len(data):
            if data[pos] != 0xFF:
                break
            marker = data[pos + 1]
            if marker in (0xD9, 0xDA):
                break
            seg_len = struct.unpack_from(">H", data, pos + 2)[0]
            seg = data[pos + 4 : pos + 2 + seg_len]
            if marker == 0xE1 and seg.startswith(b"Exif\x00\x00"):
                tiff = seg[6:]
                if len(tiff) >= 8:
                    endian = "<" if tiff[:2] == b"II" else (">" if tiff[:2] == b"MM" else "")
                    if endian:
                        ifd0_off = _read_u32(tiff, 4, endian)
                        ifd0_map = {
                            0x010F: "fabricant",
                            0x0110: "modele_appareil",
                            0x0131: "logiciel",
                            0x0132: "date_fichier_exif",
                        }
                        tags, exif_sub = _parse_ifd(tiff, ifd0_off, endian, ifd0_map)
                        exif_tags.update(tags)
                        if exif_sub is not None:
                            sub_tags, _ = _parse_ifd(
                                tiff,
                                exif_sub,
                                endian,
                                {
                                    0x9003: "date_prise_de_vue",
                                    0x9004: "date_numerisation",
                                },
                            )
                            exif_tags.update(sub_tags)
                break
            pos += 2 + seg_len

    indicateurs = ["EXIF_PRESENT"] if exif_tags else ["EXIF_ABSENT_OU_STRIPPE"]
    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": {"exif": exif_tags},
    }


def _inspect_png(path: Path) -> dict[str, object]:
    data = path.read_bytes()
    text_chunks: dict[str, str] = {}
    if data.startswith(b"\x89PNG\r\n\x1a\n"):
        pos = 8
        while pos + 12 <= len(data):
            length = struct.unpack_from(">I", data, pos)[0]
            ctype = data[pos + 4 : pos + 8]
            chunk_data = data[pos + 8 : pos + 8 + length]
            if ctype == b"tEXt" and b"\x00" in chunk_data:
                k, v = chunk_data.split(b"\x00", 1)
                text_chunks[k.decode("latin-1", errors="replace")] = _truncate(
                    v.decode("latin-1", errors="replace"), 150
                )
            pos += 12 + length
            if ctype == b"IEND":
                break
    indicateurs = ["METADONNEES_PNG_PRESENTES"] if text_chunks else []
    return {
        "statut": "ok",
        "indicateurs": indicateurs,
        "details": {"chunks_texte": text_chunks},
    }


def inspecter_fichier(path: Path) -> dict[str, object]:
    base: dict[str, object] = {"chemin": str(path)}
    if not path.exists():
        base["statut"] = "erreur"
        base["erreur"] = "Fichier introuvable."
        return base
    if not path.is_file():
        base["statut"] = "erreur"
        base["erreur"] = "Le chemin désigne un répertoire, pas un fichier."
        return base

    stat = path.stat()
    ext = path.suffix.lower()
    mime, _ = mimetypes.guess_type(path.name)
    base.update(
        {
            "nom": path.name,
            "extension": ext or "(sans extension)",
            "type_mime_presume": mime or "application/octet-stream",
            "taille_octets": stat.st_size,
            "sha256": _sha256_file(path),
        }
    )

    if ext in _DOCX_EXTS:
        spec = _inspect_docx(path)
    elif ext in _XLSX_EXTS:
        spec = _inspect_xlsx(path)
    elif ext in _EML_EXTS:
        spec = _inspect_eml(path)
    elif ext in _PDF_EXTS:
        spec = _inspect_pdf(path)
    elif ext in _JPEG_EXTS:
        spec = _inspect_jpeg(path)
    elif ext in _PNG_EXTS:
        spec = _inspect_png(path)
    else:
        spec = {
            "statut": "ok",
            "indicateurs": ["INSPECTION_GENERIQUE"],
            "details": {},
        }

    base.update(spec)
    return base


def _format_texte(resultats: list[dict[str, object]]) -> str:
    lignes: list[str] = []
    for item in resultats:
        lignes.append(f"=== {item.get('chemin')} ===")
        if item.get("statut") != "ok":
            lignes.append(f"ERREUR : {item.get('erreur')}")
            lignes.append("")
            continue
        lignes.append(
            f"Format : {item['extension']} | Taille : {item['taille_octets']} octets | SHA-256 : {str(item['sha256'])[:16]}…"
        )
        indicateurs = item.get("indicateurs") or []
        lignes.append(
            "Signaux : " + (", ".join(str(x) for x in indicateurs) if indicateurs else "aucun signal particulier")
        )
        details = item.get("details") or {}
        lignes.append(json.dumps(details, ensure_ascii=False, indent=2))
        lignes.append("")
    return "\n".join(lignes)


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    parser = argparse.ArgumentParser(
        description="Inspecter les métadonnées et structures cachées de pièces locales (.docx, .xlsx, .eml, .pdf, images)."
    )
    parser.add_argument("fichiers", nargs="+", help="Chemins des fichiers à inspecter.")
    parser.add_argument("--json", action="store_true", help="Afficher le résultat au format JSON.")
    args = parser.parse_args(argv)

    resultats = [inspecter_fichier(Path(f)) for f in args.fichiers]
    if args.json:
        print(json.dumps(resultats, ensure_ascii=False, indent=2))
    else:
        print(_format_texte(resultats), end="")

    has_error = any(r.get("statut") != "ok" for r in resultats)
    return 1 if has_error else 0


if __name__ == "__main__":
    raise SystemExit(main())
