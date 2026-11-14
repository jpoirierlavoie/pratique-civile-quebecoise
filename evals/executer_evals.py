#!/usr/bin/env python3
"""Exécuteur et vérificateur de la suite d'évaluation comportementale (« evals »).

Bibliothèque standard Python uniquement, aucun appel réseau.
Usages :
    python evals/executer_evals.py --liste
    python evals/executer_evals.py --auto-test
    python evals/executer_evals.py --reponses chemin/vers/reponses.json [--json]
"""

from __future__ import annotations

import argparse
from datetime import date, time
import importlib.util
import json
from pathlib import Path
import re
import sys
import tempfile
from typing import Any
import zipfile

RACINE = Path(__file__).resolve().parent.parent
SCENARIOS_PATH = Path(__file__).resolve().parent / "scenarios.json"


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconf = getattr(stream, "reconfigure", None)
        if callable(reconf):
            reconf(encoding="utf-8", errors="replace")


def _charger_module(rel_path: str, nom_module: str) -> Any:
    module_path = RACINE / rel_path
    spec = importlib.util.spec_from_file_location(nom_module, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Impossible de charger le module {rel_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom_module] = module
    spec.loader.exec_module(module)
    return module


def charger_scenarios(path: Path = SCENARIOS_PATH) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("scenarios"), list):
        raise ValueError(f"{path} : objet JSON avec clé 'scenarios' (liste) attendu")
    return data["scenarios"]


def evaluer_reponse(scenario: dict[str, Any], texte: str) -> dict[str, Any]:
    """Évalue une réponse textuelle par rapport aux expressions attendues et interdites."""
    manquants: list[str] = []
    interdits_trouves: list[str] = []

    for pat in scenario.get("doit_contenir", []):
        if not re.search(pat, texte, flags=re.I | re.M):
            manquants.append(pat)

    for pat in scenario.get("ne_doit_pas_contenir", []):
        if re.search(pat, texte, flags=re.I | re.M):
            interdits_trouves.append(pat)

    reussi = not manquants and not interdits_trouves
    return {
        "id": scenario["id"],
        "competence": scenario["competence"],
        "reussi": reussi,
        "manquants": manquants,
        "interdits_trouves": interdits_trouves,
    }


def _creer_fixture_docx_commentaire(dest: Path) -> None:
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        '<Override PartName="/word/comments.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
        '<Override PartName="/docProps/core.xml" '
        'ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
        "</Types>"
    )
    rels = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/>'
        '<Relationship Id="rId2" '
        'Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" '
        'Target="docProps/core.xml"/>'
        "</Relationships>"
    )
    document = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body><w:p><w:r><w:t>PROJET DE DÉFENSE — sans numéro de cour</w:t></w:r></w:p></w:body>"
        "</w:document>"
    )
    comments = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:comments xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        '<w:comment w:id="1" w:author="Me Tremblay" w:date="2026-09-10T14:20:00Z">'
        "<w:p><w:r><w:t>Ne pas produire avant d'avoir vérifié la prescription.</w:t></w:r></w:p>"
        "</w:comment></w:comments>"
    )
    core = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties '
        'xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/">'
        "<dc:creator>Me Tremblay</dc:creator>"
        "</cp:coreProperties>"
    )
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("[Content_Types].xml", content_types)
        zf.writestr("_rels/.rels", rels)
        zf.writestr("word/document.xml", document)
        zf.writestr("word/comments.xml", comments)
        zf.writestr("docProps/core.xml", core)


def executer_tests_outils(scenarios: list[dict[str, Any]]) -> list[str]:
    """Exécute les assertions déterministes attachées aux outils Python locaux."""
    erreurs: list[str] = []
    calcul_mod = _charger_module(
        "skills/calendrier-procedural/scripts/calcul_delai.py", "calcul_delai"
    )
    inspect_mod = _charger_module(
        "skills/analyse-documentaire/scripts/inspecter_piece.py", "inspecter_piece"
    )

    for sc in scenarios:
        spec = sc.get("test_outil")
        if not spec:
            continue
        sid = sc["id"]
        outil = spec.get("outil")
        if outil == "calcul_delai":
            for cas in spec.get("cas", []):
                heure_raw = cas.get("heure_notification")
                heure = time.fromisoformat(heure_raw) if heure_raw else None
                res = calcul_mod.calculer_delai(
                    ancrage=date.fromisoformat(cas["ancrage"]),
                    valeur=int(cas["valeur"]),
                    unite=cas["unite"],
                    sens=cas["sens"],
                    mode_notification=cas["mode_notification"],
                    heure_notification=heure,
                )
                att = cas["attendu"]
                for cle in (
                    "ancrage_effectif",
                    "echeance_brute",
                    "echeance",
                    "echeance_report_suivant",
                    "reportee",
                ):
                    if cle in att and res.get(cle) != att[cle]:
                        erreurs.append(
                            f"{sid} ({cas['nom']}) : {cle}={res.get(cle)!r}, attendu {att[cle]!r}"
                        )
                if "nb_reports" in att and len(res.get("reports", [])) != att["nb_reports"]:
                    erreurs.append(
                        f"{sid} ({cas['nom']}) : len(reports)={len(res.get('reports', []))}, attendu {att['nb_reports']}"
                    )
                av_blob = "\n".join(res.get("avertissements", []))
                for sous_chaine in att.get("avertissements_contient", []):
                    if sous_chaine.lower() not in av_blob.lower():
                        erreurs.append(
                            f"{sid} ({cas['nom']}) : avertissement attendu contenant {sous_chaine!r} absent"
                        )
        elif outil == "inspecter_piece":
            if spec.get("fixture") == "docx_avec_commentaire":
                with tempfile.TemporaryDirectory() as tmp:
                    docx_path = Path(tmp) / "Defense_finale.docx"
                    _creer_fixture_docx_commentaire(docx_path)
                    res = inspect_mod.inspecter_fichier(docx_path)
                    att = spec["attendu"]
                    if res.get("statut") != att.get("statut"):
                        erreurs.append(f"{sid} : statut={res.get('statut')!r}, attendu {att.get('statut')!r}")
                    inds = set(res.get("indicateurs", []))
                    for ind in att.get("indicateurs_contient", []):
                        if ind not in inds:
                            erreurs.append(f"{sid} : indicateur {ind!r} manquant ({sorted(inds)})")
                    nb_com = int(res.get("details", {}).get("nombre_commentaires", 0))
                    if nb_com < int(att.get("nombre_commentaires_min", 0)):
                        erreurs.append(f"{sid} : nombre_commentaires={nb_com} insuffisant")
        else:
            erreurs.append(f"{sid} : outil de test inconnu {outil!r}")
    return erreurs


def auto_test() -> int:
    scenarios = charger_scenarios()
    erreurs: list[str] = []

    if not scenarios:
        erreurs.append("Aucun scénario trouvé dans evals/scenarios.json.")

    for sc in scenarios:
        for champ in ("doit_contenir", "ne_doit_pas_contenir"):
            for pat in sc.get(champ, []):
                try:
                    re.compile(pat, flags=re.I | re.M)
                except re.error as exc:
                    erreurs.append(f"{sc['id']} ({champ}) : regex invalide {pat!r} ({exc})")

    erreurs.extend(executer_tests_outils(scenarios))

    # Auto-vérification du moteur d'évaluation de réponses (positif et négatif)
    sc_rj01 = next((s for s in scenarios if s["id"] == "RJ-01"), None)
    if sc_rj01 is not None:
        ok = evaluer_reponse(
            sc_rj01,
            "En droit civil québécois, la garantie de qualité relève de l'art. 1726 C.c.Q. "
            "et la dénonciation du vice de l'art. 1739 C.c.Q.",
        )
        bad = evaluer_reponse(
            sc_rj01,
            "Selon l'art. 1641 de la Cour de cassation, vous devez agir vite.",
        )
        if not ok["reussi"]:
            erreurs.append(f"Auto-test positif RJ-01 a échoué : {ok}")
        if bad["reussi"]:
            erreurs.append("Auto-test négatif RJ-01 aurait dû détecter art. 1641 / Cour de cassation.")

    if erreurs:
        for err in erreurs:
            print(err, file=sys.stderr)
        return 1

    print(
        f"Auto-test réussi : {len(scenarios)} scénarios validés, "
        "assertions déterministes de calcul_delai.py et inspecter_piece.py conformes."
    )
    return 0


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    parser = argparse.ArgumentParser(
        description="Suite d'évaluation comportementale de Pratique civile québécoise."
    )
    parser.add_argument("--liste", action="store_true", help="Lister les scénarios d'évaluation.")
    parser.add_argument(
        "--auto-test",
        action="store_true",
        help="Valider le schéma, compiler les regex et exécuter les tests d'outils déterministes.",
    )
    parser.add_argument(
        "--reponses",
        type=Path,
        default=None,
        help="Fichier JSON {id_scenario: texte_reponse} à noter selon les critères.",
    )
    parser.add_argument("--json", action="store_true", help="Sortie structurée en JSON.")
    args = parser.parse_args(argv)

    scenarios = charger_scenarios()

    if args.liste:
        if args.json:
            print(
                json.dumps(
                    [
                        {"id": s["id"], "competence": s["competence"], "titre": s["titre"]}
                        for s in scenarios
                    ],
                    ensure_ascii=False,
                    indent=2,
                )
            )
        else:
            for sc in scenarios:
                print(f"{sc['id']} | {sc['competence']} | {sc['titre']}")
        return 0

    if args.reponses is not None:
        reponses = json.loads(args.reponses.read_text(encoding="utf-8"))
        if not isinstance(reponses, dict):
            print("Erreur : le fichier de réponses doit contenir un objet JSON.", file=sys.stderr)
            return 2
        resultats = [
            evaluer_reponse(sc, str(reponses.get(sc["id"], "")))
            for sc in scenarios
            if sc["id"] in reponses
        ]
        reussis = sum(1 for r in resultats if r["reussi"])
        rapport = {
            "evalues": len(resultats),
            "reussis": reussis,
            "echoues": len(resultats) - reussis,
            "details": resultats,
        }
        if args.json:
            print(json.dumps(rapport, ensure_ascii=False, indent=2))
        else:
            print(f"Score : {reussis}/{len(resultats)}")
            for r in resultats:
                etat = "OK" if r["reussi"] else "ECHEC"
                print(f"[{etat}] {r['id']} ({r['competence']})")
                if r["manquants"]:
                    print(f"  Manquants : {r['manquants']}")
                if r["interdits_trouves"]:
                    print(f"  Interdits : {r['interdits_trouves']}")
        return 0 if reussis == len(resultats) and resultats else 1

    return auto_test()


if __name__ == "__main__":
    raise SystemExit(main())
