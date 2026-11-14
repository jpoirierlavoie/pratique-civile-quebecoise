"""Contrôle statique du dépôt « Pratique civile québécoise ».

Exécuter depuis la racine du dépôt :

    python verifier.py

Ne retourne rien (code de sortie 0) lorsque tout est conforme ; écrit une
ligne d'erreur par manquement sur la sortie d'erreur standard (code 1) sinon.
"""

from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

ROOT_ALLOWLIST = frozenset(
    {
        ".gitattributes",
        ".gitignore",
        ".github/workflows/verify.yml",
        ".claude-plugin/plugin.json",
        ".claude-plugin/marketplace.json",
        "plugin.json",
        "mcp_config.json",
        "gemini-extension.json",
        ".mcp.json",
        "assets/logo.svg",
        "LICENSE",
        "README.md",
        "verifier.py",
    }
)

EVALS_ALLOWLIST = frozenset(
    {
        "evals/README.md",
        "evals/scenarios.json",
        "evals/executer_evals.py",
    }
)

ANTIGRAVITY_PLUGIN_KEYS = frozenset(
    {
        "name",
        "displayName",
        "version",
        "description",
        "logo",
        "suggestedPrompts",
        "author",
        "homepage",
        "repository",
        "disabled",
    }
)

ANTIGRAVITY_AUTHOR_KEYS = frozenset({"name", "url"})

EXPECTED_PLUGIN_NAME = "pratique-civile-quebecoise"
EXPECTED_REPO_URL = "https://github.com/jpoirierlavoie/pratique-civile-quebecoise"
RETIRED_REPO_SLUGS = (
    "competence-litige-civil",
    "competence-pratique-civile-quebecoise",
)
EXPECTED_LICENSE = "CC0-1.0"
EXPECTED_OUTILS_URL = "https://outils.poirierlavoie.ca/mcp"
EXPECTED_MCP_SERVERS = {
    "Legislation": {},
    "Jurisprudence": {},
    "pratique-civile-outils": {"type": "http", "url": EXPECTED_OUTILS_URL},
}
EXPECTED_LEGISLATION_URL = "https://legislation.poirierlavoie.ca/mcp"
EXPECTED_LEGISLATION_AUTH = "Bearer $" + "{MCP_LEGISLATION_SECRET}"
EXPECTED_JURISPRUDENCE_URL = "https://jurisprudence.poirierlavoie.ca/mcp"
EXPECTED_JURISPRUDENCE_AUTH = "Bearer $" + "{MCP_JURISPRUDENCE_SECRET}"
EXPECTED_GOOGLE_SERVERS = {
    "legislation": (
        EXPECTED_LEGISLATION_URL,
        EXPECTED_LEGISLATION_AUTH,
        "MCP_LEGISLATION_SECRET",
    ),
    "jurisprudence": (
        EXPECTED_JURISPRUDENCE_URL,
        EXPECTED_JURISPRUDENCE_AUTH,
        "MCP_JURISPRUDENCE_SECRET",
    ),
}
_HEX_SECRET_RE = re.compile(r"[0-9a-f]{32,}", re.I)
ALLOWED_TOOL_PREFIXES = frozenset(
    {"legislation", "jurisprudence", "greffe", "palais", "calendrier", "interets"}
)

BANNED_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("mention de pallas-athena", re.compile(r"pallas[-_]athena", re.I)),
    ("mention d'athena", re.compile(r"\bathena\b", re.I)),
    ("préfixe mcp__", re.compile(r"\bmcp__", re.I)),
    ("préfixe qclaw_", re.compile(r"\bqclaw_", re.I)),
    ("préfixe canlii_", re.compile(r"\bcanlii_", re.I)),
    ("variable Claude $ARGUMENTS", re.compile(r"\$ARGUMENTS\b")),
    ("variable ${CLAUDE_...", re.compile(r"\$\{CLAUDE_")),
    (
        "artefact de sous-agent (<usage> / agentId)",
        re.compile(r"</?usage>|\bagentId:\s*[0-9a-f]+", re.I),
    ),
    (
        "nom d'outil de gestionnaire de dossiers",
        re.compile(
            r"\b(?:"
            r"get_dossier|list_dossiers|search_dossiers|create_dossier|update_dossier|"
            r"create_note|update_note|begin_upload|finalize_upload|"
            r"create_task|create_hearing|create_invoice"
            r")\b"
        ),
    ),
)

_SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
_SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")
_REF_PATH_RE = re.compile(r"references/[a-z0-9-]+\.md")
_SCRIPT_PATH_RE = re.compile(r"scripts/[a-z0-9_-]+\.py")
_SCRIPT_NAME_RE = re.compile(r"^[a-z0-9_]+\.py$")
_CROSS_SKILL_RE = re.compile(
    r"(?:(?:voir|relève\s+de)\s+`?([a-z0-9]+-[a-z0-9-]+)`?|`([a-z0-9]+-[a-z0-9-]+)`)"
)
_BACKTICK_SPAN_RE = re.compile(r"`([^`\n]+)`")
_TOOL_SPAN_RE = re.compile(r"^([a-z][a-z0-9_]*)_")
_FENCE_RE = re.compile(r"(?ms)^```[^\n]*\n.*?^```\s*$")


def _extract_h2_headings(body: str) -> list[str]:
    stripped = _FENCE_RE.sub("", body)
    return [line.strip() for line in stripped.splitlines() if line.startswith("## ")]


def _iter_repo_files(racine: Path) -> list[str]:
    files: list[str] = []
    for path in sorted(racine.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(racine).as_posix()
        parts = rel.split("/")
        if ".git" in parts or "__pycache__" in parts:
            continue
        files.append(rel)
    return files


def _parse_frontmatter(text: str, rel: str) -> tuple[dict[str, str] | None, str, list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n"):
        return None, text, [f"{rel} : en-tête YAML absent"]
    end_idx = text.find("\n---\n", 4)
    if end_idx < 0:
        return None, text, [f"{rel} : fermeture '---' de l'en-tête YAML introuvable"]

    fm_lines = text[4:end_idx].split("\n")
    body = text[end_idx + 5 :]
    data: dict[str, str] = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[0] in (" ", "\t"):
            errors.append(f"{rel} : indentation inattendue dans l'en-tête YAML à la ligne {i + 2}")
            i += 1
            continue
        if ":" not in line:
            errors.append(f"{rel} : ligne YAML invalide à la ligne {i + 2}")
            i += 1
            continue
        key, rest = line.split(":", 1)
        key = key.strip()
        val_raw = rest.strip()
        if val_raw in (">-", ">", "|-", "|"):
            fold = val_raw.startswith(">")
            block: list[str] = []
            i += 1
            while i < len(fm_lines):
                nxt = fm_lines[i]
                if not nxt.strip():
                    block.append("")
                    i += 1
                    continue
                if nxt[0] in (" ", "\t"):
                    block.append(nxt.strip())
                    i += 1
                    continue
                break
            if fold:
                paras: list[str] = []
                cur: list[str] = []
                for b in block:
                    if b == "":
                        if cur:
                            paras.append(" ".join(cur))
                            cur = []
                        paras.append("")
                    else:
                        cur.append(b)
                if cur:
                    paras.append(" ".join(cur))
                data[key] = "\n".join(paras).strip()
            else:
                data[key] = "\n".join(block).strip()
            continue
        if (val_raw.startswith('"') and val_raw.endswith('"')) or (
            val_raw.startswith("'") and val_raw.endswith("'")
        ):
            val_raw = val_raw[1:-1]
        data[key] = val_raw
        i += 1

    return data, body, errors


def _load_json(racine: Path, rel: str, erreurs: list[str]) -> dict | None:
    path = racine / rel
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        erreurs.append(f"{rel} : JSON invalide ({exc})")
        return None
    if not isinstance(data, dict):
        erreurs.append(f"{rel} : objet JSON attendu à la racine")
        return None
    return data


def verifier(racine: Path) -> list[str]:
    erreurs: list[str] = []
    files = _iter_repo_files(racine)
    file_set = set(files)

    # 1. File inventory & allowlist
    for rel in sorted(ROOT_ALLOWLIST | EVALS_ALLOWLIST):
        if rel not in file_set:
            erreurs.append(f"fichier requis manquant : {rel}")

    skill_md_files: list[str] = []
    skill_script_files: list[str] = []
    eval_files: list[str] = []
    for rel in files:
        if rel in ROOT_ALLOWLIST:
            continue
        if rel in EVALS_ALLOWLIST:
            eval_files.append(rel)
            continue
        parts = rel.split("/")
        if len(parts) == 3 and parts[0] == "skills" and parts[2] == "SKILL.md":
            skill_md_files.append(rel)
            continue
        if (
            len(parts) == 4
            and parts[0] == "skills"
            and parts[2] == "references"
            and parts[3].endswith(".md")
        ):
            skill_md_files.append(rel)
            continue
        if (
            len(parts) == 4
            and parts[0] == "skills"
            and parts[2] == "scripts"
            and parts[3].endswith(".py")
        ):
            skill_script_files.append(rel)
            continue
        erreurs.append(f"fichier hors inventaire autorisé : {rel}")

    # 2. Encoding (UTF-8 without BOM, LF only except LICENSE)
    decoded: dict[str, str] = {}
    for rel in files:
        raw = (racine / rel).read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            erreurs.append(f"{rel} : BOM UTF-8 interdit")
            continue
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            erreurs.append(f"{rel} : encodage UTF-8 invalide")
            continue
        if rel != "LICENSE" and "\r" in text:
            erreurs.append(f"{rel} : fins de ligne CR/CRLF interdites (LF requis)")
        decoded[rel] = text

    # 3. Manifest consistency
    claude_plugin = _load_json(racine, ".claude-plugin/plugin.json", erreurs)
    marketplace = _load_json(racine, ".claude-plugin/marketplace.json", erreurs)
    agy_plugin = _load_json(racine, "plugin.json", erreurs)
    agy_mcp = _load_json(racine, "mcp_config.json", erreurs)
    gemini_ext = _load_json(racine, "gemini-extension.json", erreurs)
    mcp_json = _load_json(racine, ".mcp.json", erreurs)

    for rel_mcp in (".mcp.json", "mcp_config.json", "gemini-extension.json"):
        brut = decoded.get(rel_mcp)
        if brut is not None and _HEX_SECRET_RE.search(brut):
            erreurs.append(f"{rel_mcp} : secret hexadécimal potentiel détecté")

    versions: dict[str, str] = {}

    if claude_plugin is not None:
        if claude_plugin.get("name") != EXPECTED_PLUGIN_NAME:
            erreurs.append(
                f".claude-plugin/plugin.json : 'name' doit valoir '{EXPECTED_PLUGIN_NAME}'"
            )
        ver = claude_plugin.get("version")
        if not isinstance(ver, str) or not _SEMVER_RE.match(ver):
            erreurs.append(".claude-plugin/plugin.json : 'version' semver invalide")
        else:
            versions[".claude-plugin/plugin.json"] = ver
        if claude_plugin.get("license") != EXPECTED_LICENSE:
            erreurs.append(
                f".claude-plugin/plugin.json : 'license' doit valoir '{EXPECTED_LICENSE}'"
            )
        for field in ("homepage", "repository"):
            if claude_plugin.get(field) != EXPECTED_REPO_URL:
                erreurs.append(
                    f".claude-plugin/plugin.json : '{field}' doit valoir '{EXPECTED_REPO_URL}'"
                )

    if marketplace is not None:
        if marketplace.get("name") != EXPECTED_PLUGIN_NAME:
            erreurs.append(
                f".claude-plugin/marketplace.json : 'name' doit valoir '{EXPECTED_PLUGIN_NAME}'"
            )
        plugins_list = marketplace.get("plugins")
        if not isinstance(plugins_list, list) or len(plugins_list) != 1 or not isinstance(
            plugins_list[0], dict
        ):
            erreurs.append(
                ".claude-plugin/marketplace.json : 'plugins' doit contenir exactement un objet"
            )
        else:
            entry = plugins_list[0]
            if entry.get("name") != EXPECTED_PLUGIN_NAME:
                erreurs.append(
                    ".claude-plugin/marketplace.json : plugins[0].name doit valoir "
                    f"'{EXPECTED_PLUGIN_NAME}'"
                )
            ver = entry.get("version")
            if not isinstance(ver, str) or not _SEMVER_RE.match(ver):
                erreurs.append(
                    ".claude-plugin/marketplace.json : plugins[0].version semver invalide"
                )
            else:
                versions[".claude-plugin/marketplace.json"] = ver
            if entry.get("license") != EXPECTED_LICENSE:
                erreurs.append(
                    ".claude-plugin/marketplace.json : plugins[0].license doit valoir "
                    f"'{EXPECTED_LICENSE}'"
                )
            if entry.get("source") != "./":
                erreurs.append(
                    ".claude-plugin/marketplace.json : plugins[0].source doit valoir './'"
                )
            for field in ("homepage", "repository"):
                if entry.get(field) != EXPECTED_REPO_URL:
                    erreurs.append(
                        f".claude-plugin/marketplace.json : plugins[0].{field} doit valoir '{EXPECTED_REPO_URL}'"
                    )

    if agy_plugin is not None:
        unknown_keys = sorted(set(agy_plugin) - ANTIGRAVITY_PLUGIN_KEYS)
        if unknown_keys:
            erreurs.append(
                f"plugin.json : clés non reconnues par Antigravity : {', '.join(unknown_keys)}"
            )
        if agy_plugin.get("name") != EXPECTED_PLUGIN_NAME:
            erreurs.append(f"plugin.json : 'name' doit valoir '{EXPECTED_PLUGIN_NAME}'")
        ver = agy_plugin.get("version")
        if not isinstance(ver, str) or not _SEMVER_RE.match(ver):
            erreurs.append("plugin.json : 'version' semver invalide")
        else:
            versions["plugin.json"] = ver
        for field in ("homepage", "repository"):
            if agy_plugin.get(field) != EXPECTED_REPO_URL:
                erreurs.append(
                    f"plugin.json : '{field}' doit valoir '{EXPECTED_REPO_URL}'"
                )
        author = agy_plugin.get("author")
        if isinstance(author, dict):
            bad_author = sorted(set(author) - ANTIGRAVITY_AUTHOR_KEYS)
            if bad_author:
                erreurs.append(
                    f"plugin.json : clés non supportées dans author : {', '.join(bad_author)}"
                )
        elif author is not None and not isinstance(author, str):
            erreurs.append("plugin.json : 'author' doit être une chaîne ou un objet")
        logo = agy_plugin.get("logo")
        if not isinstance(logo, str) or not logo or logo.startswith("/") or "://" in logo:
            erreurs.append("plugin.json : 'logo' doit être un chemin relatif valide")
        elif not (racine / logo).is_file():
            erreurs.append(f"plugin.json : fichier logo introuvable ({logo})")
        prompts = agy_plugin.get("suggestedPrompts")
        if (
            not isinstance(prompts, list)
            or not (1 <= len(prompts) <= 3)
            or any(not isinstance(p, str) or not p.strip() for p in prompts)
        ):
            erreurs.append(
                "plugin.json : 'suggestedPrompts' doit contenir entre 1 et 3 chaînes non vides"
            )

    if agy_mcp is not None:
        agy_servers = agy_mcp.get("mcpServers")
        if not isinstance(agy_servers, dict) or set(agy_servers.keys()) != {
            "jurisprudence",
            "pratique-civile-outils",
        }:
            erreurs.append(
                "mcp_config.json : 'mcpServers' doit déclarer exactement "
                "'jurisprudence' et 'pratique-civile-outils'"
            )
        else:
            srv = agy_servers["jurisprudence"]
            if not isinstance(srv, dict):
                erreurs.append("mcp_config.json : mcpServers.jurisprudence doit être un objet JSON")
            else:
                if srv.get("url") != EXPECTED_JURISPRUDENCE_URL:
                    erreurs.append(
                        f"mcp_config.json : url doit valoir '{EXPECTED_JURISPRUDENCE_URL}'"
                    )
                if srv.get("headers") != {"Authorization": EXPECTED_JURISPRUDENCE_AUTH}:
                    erreurs.append(
                        "mcp_config.json : headers.Authorization doit valoir "
                        f"'{EXPECTED_JURISPRUDENCE_AUTH}'"
                    )
                if "eager" in srv:
                    erreurs.append("mcp_config.json : 'eager' doit être omis (chargement paresseux)")
                variables = srv.get("variables")
                has_secret_var = isinstance(variables, list) and any(
                    isinstance(v, dict)
                    and v.get("name") == "MCP_JURISPRUDENCE_SECRET"
                    and isinstance(v.get("title"), str)
                    and bool(v["title"].strip())
                    and isinstance(v.get("description"), str)
                    and bool(v["description"].strip())
                    for v in variables
                )
                if not has_secret_var:
                    erreurs.append(
                        "mcp_config.json : variables doit déclarer MCP_JURISPRUDENCE_SECRET "
                        "avec 'title' et 'description'"
                    )
            outils_srv = agy_servers["pratique-civile-outils"]
            if not isinstance(outils_srv, dict):
                erreurs.append(
                    "mcp_config.json : mcpServers.pratique-civile-outils doit être un objet JSON"
                )
            else:
                if "eager" in outils_srv:
                    erreurs.append(
                        "mcp_config.json : mcpServers.pratique-civile-outils ne doit pas "
                        "contenir 'eager'"
                    )
                if outils_srv.get("url") != EXPECTED_OUTILS_URL:
                    erreurs.append(
                        "mcp_config.json : mcpServers.pratique-civile-outils.url doit valoir "
                        f"'{EXPECTED_OUTILS_URL}'"
                    )
                if set(outils_srv.keys()) != {"url"}:
                    erreurs.append(
                        "mcp_config.json : mcpServers.pratique-civile-outils ne doit contenir "
                        "que la clé 'url'"
                    )

    if gemini_ext is not None:
        if gemini_ext.get("name") != EXPECTED_PLUGIN_NAME:
            erreurs.append(
                f"gemini-extension.json : 'name' doit valoir '{EXPECTED_PLUGIN_NAME}'"
            )
        ver = gemini_ext.get("version")
        if not isinstance(ver, str) or not _SEMVER_RE.match(ver):
            erreurs.append("gemini-extension.json : 'version' semver invalide")
        else:
            versions["gemini-extension.json"] = ver
        g_servers = gemini_ext.get("mcpServers")
        if not isinstance(g_servers, dict) or set(g_servers.keys()) != {
            "jurisprudence",
            "pratique-civile-outils",
        }:
            erreurs.append(
                "gemini-extension.json : 'mcpServers' doit déclarer exactement "
                "'jurisprudence' et 'pratique-civile-outils'"
            )
        else:
            gsrv = g_servers["jurisprudence"]
            if not isinstance(gsrv, dict):
                erreurs.append(
                    "gemini-extension.json : mcpServers.jurisprudence doit être un objet JSON"
                )
            else:
                if gsrv.get("httpUrl") != EXPECTED_JURISPRUDENCE_URL:
                    erreurs.append(
                        f"gemini-extension.json : httpUrl doit valoir '{EXPECTED_JURISPRUDENCE_URL}'"
                    )
                if gsrv.get("headers") != {"Authorization": EXPECTED_JURISPRUDENCE_AUTH}:
                    erreurs.append(
                        "gemini-extension.json : headers.Authorization doit valoir "
                        f"'{EXPECTED_JURISPRUDENCE_AUTH}'"
                    )
            g_outils = g_servers["pratique-civile-outils"]
            if not isinstance(g_outils, dict):
                erreurs.append(
                    "gemini-extension.json : mcpServers.pratique-civile-outils doit être "
                    "un objet JSON"
                )
            else:
                if g_outils.get("httpUrl") != EXPECTED_OUTILS_URL:
                    erreurs.append(
                        "gemini-extension.json : mcpServers.pratique-civile-outils.httpUrl "
                        f"doit valoir '{EXPECTED_OUTILS_URL}'"
                    )
                if set(g_outils.keys()) != {"httpUrl"}:
                    erreurs.append(
                        "gemini-extension.json : mcpServers.pratique-civile-outils ne doit "
                        "contenir que la clé 'httpUrl'"
                    )
        settings = gemini_ext.get("settings")
        has_secret_setting = isinstance(settings, list) and any(
            isinstance(s, dict)
            and s.get("envVar") == "MCP_JURISPRUDENCE_SECRET"
            and s.get("sensitive") is True
            and isinstance(s.get("name"), str)
            and bool(s["name"].strip())
            and isinstance(s.get("description"), str)
            and bool(s["description"].strip())
            for s in settings
        )
        if not has_secret_setting:
            erreurs.append(
                "gemini-extension.json : settings doit déclarer MCP_JURISPRUDENCE_SECRET "
                "avec sensitive=true, 'name' et 'description'"
            )

    if len(set(versions.values())) > 1:
        detail = ", ".join(f"{k}={v}" for k, v in sorted(versions.items()))
        erreurs.append(f"versions divergentes entre manifestes : {detail}")

    if mcp_json is not None:
        if mcp_json.get("mcpServers") != EXPECTED_MCP_SERVERS:
            erreurs.append(
                ".mcp.json : 'mcpServers' doit déclarer exactement Legislation: {}, "
                "Jurisprudence: {} et pratique-civile-outils"
            )

    # 4. Skills & references
    skills_root = racine / "skills"
    skill_dirs = (
        sorted(p.name for p in skills_root.iterdir() if p.is_dir())
        if skills_root.is_dir()
        else []
    )
    if not skill_dirs:
        erreurs.append("aucune compétence trouvée sous skills/")
        return erreurs

    skill_dir_set = set(skill_dirs)

    for skill in skill_dirs:
        if len(skill) > 64 or not _SKILL_NAME_RE.match(skill):
            erreurs.append(f"skills/{skill} : nom de dossier invalide (kebab-case ≤ 64 car.)")
        skill_rel = f"skills/{skill}/SKILL.md"
        if skill_rel not in file_set:
            erreurs.append(f"skills/{skill} : SKILL.md manquant")
            continue
        text = decoded.get(skill_rel)
        if text is None:
            continue

        fm, body, fm_errs = _parse_frontmatter(text, skill_rel)
        erreurs.extend(fm_errs)
        if fm is not None:
            if set(fm.keys()) != {"name", "description"}:
                erreurs.append(
                    f"{skill_rel} : l'en-tête YAML doit contenir exactement 'name' et "
                    "'description'"
                )
            if fm.get("name") != skill:
                erreurs.append(
                    f"{skill_rel} : 'name' ({fm.get('name')!r}) doit correspondre au dossier "
                    f"({skill!r})"
                )
            desc = fm.get("description", "")
            if not desc:
                erreurs.append(f"{skill_rel} : 'description' vide")
            else:
                if len(desc) > 1024:
                    erreurs.append(
                        f"{skill_rel} : 'description' dépasse 1 024 caractères ({len(desc)})"
                    )
                if "<" in desc or ">" in desc:
                    erreurs.append(f"{skill_rel} : 'description' ne doit contenir ni '<' ni '>'")
                if "En anglais" not in desc:
                    erreurs.append(f"{skill_rel} : 'description' doit inclure 'En anglais'")
                if "Ne pas utiliser pour" not in desc:
                    erreurs.append(
                        f"{skill_rel} : 'description' doit inclure 'Ne pas utiliser pour'"
                    )

        words = len(body.split())
        if words >= 3000:
            erreurs.append(f"{skill_rel} : corps de {words} mots (plafond < 3 000)")

        refs_mentioned = set(_REF_PATH_RE.findall(text))
        refs_dir = racine / "skills" / skill / "references"
        refs_actual = (
            {f"references/{p.name}" for p in refs_dir.iterdir() if p.is_file()}
            if refs_dir.is_dir()
            else set()
        )
        missing_refs = sorted(refs_mentioned - refs_actual)
        orphan_refs = sorted(refs_actual - refs_mentioned)
        if missing_refs:
            erreurs.append(
                f"{skill_rel} : fichiers de référence cités mais absents : "
                + ", ".join(missing_refs)
            )
        if orphan_refs:
            erreurs.append(
                f"{skill_rel} : fichiers de référence non cités dans SKILL.md : "
                + ", ".join(orphan_refs)
            )

        scripts_mentioned = set(_SCRIPT_PATH_RE.findall(text))
        scripts_dir = racine / "skills" / skill / "scripts"
        scripts_actual: set[str] = set()
        if scripts_dir.is_dir():
            for p in scripts_dir.iterdir():
                if not p.is_file():
                    continue
                if not _SCRIPT_NAME_RE.match(p.name):
                    erreurs.append(
                        f"skills/{skill}/scripts/{p.name} : nom de script invalide "
                        "(minuscules, chiffres, '_' et '.py' requis)"
                    )
                    continue
                scripts_actual.add(f"scripts/{p.name}")
                script_rel = f"skills/{skill}/scripts/{p.name}"
                script_src = decoded.get(script_rel)
                if script_src is not None:
                    try:
                        ast.parse(script_src, filename=script_rel)
                    except SyntaxError as exc:
                        erreurs.append(
                            f"{script_rel} : erreur de syntaxe Python à la ligne {exc.lineno} ({exc.msg})"
                        )
        missing_scripts = sorted(scripts_mentioned - scripts_actual)
        orphan_scripts = sorted(scripts_actual - scripts_mentioned)
        if missing_scripts:
            erreurs.append(
                f"{skill_rel} : scripts cités mais absents : " + ", ".join(missing_scripts)
            )
        if orphan_scripts:
            erreurs.append(
                f"{skill_rel} : scripts non cités dans SKILL.md : " + ", ".join(orphan_scripts)
            )

        # Cross-skill references
        for m in _CROSS_SKILL_RE.finditer(text):
            directed = m.group(1)
            backticked = m.group(2)
            if directed is not None and directed not in skill_dir_set:
                erreurs.append(
                    f"{skill_rel} : renvoi vers une compétence inexistante ({directed})"
                )
            elif backticked is not None and backticked in skill_dir_set:
                continue

        # 7-invariant structural contract
        non_empty_lines = [line.strip() for line in body.splitlines() if line.strip()]
        if not non_empty_lines or not non_empty_lines[0].startswith("# "):
            erreurs.append(f"{skill_rel} : titre '# ' d'ouverture manquant")
        first_h2 = body.find("\n## ")
        intro_zone = body[:first_h2] if first_h2 >= 0 else body
        intro_lines = [
            line.strip()
            for line in intro_zone.splitlines()
            if line.strip() and not line.strip().startswith("# ")
        ]
        if not intro_lines:
            erreurs.append(f"{skill_rel} : texte introductif manquant sous le titre '# '")

        h2 = _extract_h2_headings(body)
        if len(h2) < 6:
            erreurs.append(
                f"{skill_rel} : ossature incomplète ({len(h2)} sections '## ', au moins 6 requises)"
            )
        else:
            if h2[0] not in ("## Le principe qui gouverne", "## La règle asymétrique"):
                erreurs.append(
                    f"{skill_rel} : premier intertitre '## ' invalide ({h2[0]!r})"
                )
            core_h2 = h2[:-3]
            if "## La méthode" not in core_h2:
                erreurs.append(f"{skill_rel} : section '## La méthode' manquante avant le triptyque final")
            if "## Ce qu'il faut du dossier" not in core_h2:
                erreurs.append(
                    f"{skill_rel} : section '## Ce qu'il faut du dossier' manquante avant le triptyque final"
                )
            if (
                "## La méthode" in core_h2
                and "## Ce qu'il faut du dossier" in core_h2
                and core_h2.index("## La méthode") > core_h2.index("## Ce qu'il faut du dossier")
            ):
                erreurs.append(
                    f"{skill_rel} : '## La méthode' doit précéder '## Ce qu'il faut du dossier'"
                )
            if h2[-3] != "## Le périmètre":
                erreurs.append(
                    f"{skill_rel} : antépénultième section attendue '## Le périmètre' (trouvé {h2[-3]!r})"
                )
            if h2[-2] != "## Contrôle avant remise":
                erreurs.append(
                    f"{skill_rel} : avant-dernière section attendue '## Contrôle avant remise' "
                    f"(trouvé {h2[-2]!r})"
                )
            expected_last = (
                "## Fichiers de référence et outillage local"
                if scripts_actual
                else "## Fichiers de référence"
            )
            if h2[-1] != expected_last:
                erreurs.append(
                    f"{skill_rel} : dernière section attendue {expected_last!r} (trouvé {h2[-1]!r})"
                )

    # 5. Evals validation
    eval_py_rel = "evals/executer_evals.py"
    if eval_py_rel in decoded:
        try:
            ast.parse(decoded[eval_py_rel], filename=eval_py_rel)
        except SyntaxError as exc:
            erreurs.append(
                f"{eval_py_rel} : erreur de syntaxe Python à la ligne {exc.lineno} ({exc.msg})"
            )

    eval_json_rel = "evals/scenarios.json"
    eval_data = _load_json(racine, eval_json_rel, erreurs)
    if eval_data is not None:
        scenarios = eval_data.get("scenarios")
        if not isinstance(scenarios, list) or not scenarios:
            erreurs.append(f"{eval_json_rel} : 'scenarios' doit être une liste non vide")
        else:
            seen_ids: set[str] = set()
            for idx, sc in enumerate(scenarios):
                if not isinstance(sc, dict):
                    erreurs.append(f"{eval_json_rel} : scenarios[{idx}] doit être un objet JSON")
                    continue
                sid = sc.get("id")
                if not isinstance(sid, str) or not sid.strip():
                    erreurs.append(f"{eval_json_rel} : scenarios[{idx}].id invalide")
                elif sid in seen_ids:
                    erreurs.append(f"{eval_json_rel} : identifiant en double ({sid!r})")
                else:
                    seen_ids.add(sid)
                comp = sc.get("competence")
                if comp not in skill_dir_set:
                    erreurs.append(
                        f"{eval_json_rel} ({sid}) : compétence inconnue ({comp!r})"
                    )
                for req_str in ("titre", "prompt"):
                    val = sc.get(req_str)
                    if not isinstance(val, str) or not val.strip():
                        erreurs.append(
                            f"{eval_json_rel} ({sid}) : champ '{req_str}' requis et non vide"
                        )
                crit = sc.get("criteres")
                if not isinstance(crit, list) or not crit or any(
                    not isinstance(c, str) or not c.strip() for c in crit
                ):
                    erreurs.append(
                        f"{eval_json_rel} ({sid}) : 'criteres' doit contenir au moins une chaîne"
                    )
                for pat_field in ("doit_contenir", "ne_doit_pas_contenir"):
                    pats = sc.get(pat_field)
                    if not isinstance(pats, list) or any(not isinstance(p, str) for p in pats):
                        erreurs.append(
                            f"{eval_json_rel} ({sid}) : '{pat_field}' doit être une liste de chaînes"
                        )
                        continue
                    for pat in pats:
                        try:
                            re.compile(pat, flags=re.I | re.M)
                        except re.error as exc:
                            erreurs.append(
                                f"{eval_json_rel} ({sid}) : regex invalide dans '{pat_field}' "
                                f"({pat!r} : {exc})"
                            )

    # Retired repository slugs across all files except verifier.py
    for rel in files:
        if rel == "verifier.py":
            continue
        text = decoded.get(rel)
        if text is None:
            continue
        for slug in RETIRED_REPO_SLUGS:
            if slug in text:
                erreurs.append(f"{rel} : ancien identifiant de dépôt interdit ({slug})")

    # Information-contract isolation across all files in skills/ and evals/
    for rel in sorted(skill_md_files + skill_script_files + eval_files):
        text = decoded.get(rel)
        if text is None:
            continue
        for label, pat in BANNED_PATTERNS:
            if pat.search(text):
                erreurs.append(f"{rel} : {label} interdit")
    for rel in sorted(skill_md_files):
        text = decoded.get(rel)
        if text is None:
            continue
        for span in _BACKTICK_SPAN_RE.findall(text):
            m = _TOOL_SPAN_RE.match(span)
            if m and (span.endswith("_") or span.endswith("_*") or "(" in span):
                prefix = span.split("_", 1)[0]
                if prefix not in ALLOWED_TOOL_PREFIXES:
                    erreurs.append(f"{rel} : appel ou préfixe d'outil non autorisé ({span})")

    return erreurs


def main() -> int:
    racine = Path(__file__).resolve().parent
    erreurs = verifier(racine)
    if erreurs:
        for err in erreurs:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
