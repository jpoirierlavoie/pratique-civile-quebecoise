#!/usr/bin/env python3
"""Calculateur déterministe de délais en procédure civile québécoise (art. 82, 83, 107 al. 4 et 111 al. 2 C.p.c.).

Bibliothèque standard Python uniquement, aucun appel réseau.
Usage CLI :
    python scripts/calcul_delai.py 2026-07-03 --jours 30 --technologique --heure 17:40 --json
"""

from __future__ import annotations

import argparse
import calendar
from datetime import date, time, timedelta
import json
import sys
from typing import Any, Iterable, Literal


def _configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconf = getattr(stream, "reconfigure", None)
        if callable(reconf):
            reconf(encoding="utf-8", errors="replace")


def _paques_gregorienne(annee: int) -> date:
    """Calcule le dimanche de Pâques selon l'algorithme grégorien anonyme."""
    a = annee % 19
    b, c = divmod(annee, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    ell = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * ell) // 451
    mois, jour_m1 = divmod(h + ell - 7 * m + 114, 31)
    return date(annee, mois, jour_m1 + 1)


def _nieme_lundi_du_mois(annee: int, mois: int, n: int) -> date:
    """Retourne le nième lundi d'un mois donné (1er = 1, 2e = 2)."""
    premier = date(annee, mois, 1)
    decalage = (0 - premier.weekday()) % 7
    return premier + timedelta(days=decalage + (n - 1) * 7)


def _lundi_precedant_25_mai(annee: int) -> date:
    """Retourne le lundi précédant le 25 mai (Journée nationale des patriotes)."""
    mai25 = date(annee, 5, 25)
    recul = mai25.weekday() or 7
    return mai25 - timedelta(days=recul)


def jours_feries_quebec(
    annee: int,
    fetes_additionnelles: Iterable[date] = (),
) -> dict[date, str]:
    """Retourne la table des jours fériés légaux au Québec pour une année civile.

    Fondements : art. 82 al. 1 C.p.c. et art. 61 (23°) de la Loi d'interprétation
    (RLRQ, c. I-16). Le 30 septembre (férié fédéral), le 24 décembre et le 31 décembre
    n'en font pas partie par défaut.
    """
    paques = _paques_gregorienne(annee)
    juillet_1 = date(annee, 7, 1)
    fete_canada = date(annee, 7, 2) if juillet_1.weekday() == 6 else juillet_1

    feries: dict[date, str] = {
        date(annee, 1, 1): "1er janvier — Jour de l'an (art. 61 (23°) b) I-16)",
        date(annee, 1, 2): "2 janvier — considéré jour férié en procédure civile (art. 82 al. 1 C.p.c.)",
        paques - timedelta(days=2): "Vendredi saint (art. 61 (23°) c) I-16)",
        paques + timedelta(days=1): "Lundi de Pâques (art. 61 (23°) d) I-16)",
        _lundi_precedant_25_mai(annee): "Lundi précédant le 25 mai — Journée nationale des patriotes (art. 61 (23°) i) I-16)",
        date(annee, 6, 24): "24 juin — Fête nationale du Québec (art. 61 (23°) e) I-16)",
        fete_canada: (
            "2 juillet — lendemain du 1er juillet qui tombe un dimanche (art. 61 (23°) f) I-16)"
            if fete_canada.day == 2
            else "1er juillet — Fête du Canada (art. 61 (23°) f) I-16)"
        ),
        _nieme_lundi_du_mois(annee, 9, 1): "1er lundi de septembre — Fête du Travail (art. 61 (23°) g) I-16)",
        _nieme_lundi_du_mois(annee, 10, 2): "2e lundi d'octobre — Action de grâces (art. 61 (23°) g.1) I-16)",
        date(annee, 12, 25): "25 décembre — Noël (art. 61 (23°) h) I-16)",
        date(annee, 12, 26): "26 décembre — considéré jour férié en procédure civile (art. 82 al. 1 C.p.c.)",
    }
    for extra in fetes_additionnelles:
        if extra.year == annee and extra not in feries:
            feries[extra] = "Fête ou fermeture additionnelle fournie (proclamation/directive)"
    return feries


def est_jour_ouvrable(
    jour: date,
    fetes_additionnelles: Iterable[date] = (),
) -> tuple[bool, str | None]:
    """Indique si une date est un jour ouvrable aux fins de l'art. 83 al. 3 C.p.c."""
    extras = tuple(fetes_additionnelles)
    feries = jours_feries_quebec(jour.year, extras)
    if jour in feries:
        return False, feries[jour]
    if jour.weekday() == 5:
        return False, "Samedi (art. 82 al. 1 et 83 al. 3 C.p.c.)"
    if jour.weekday() == 6:
        return False, "Dimanche — jour férié (art. 61 (23°) a) I-16 et art. 83 al. 3 C.p.c.)"
    return True, None


def _prochain_jour_ouvrable(
    jour: date,
    fetes_additionnelles: Iterable[date] = (),
) -> tuple[date, list[dict[str, str]]]:
    extras = tuple(fetes_additionnelles)
    courant = jour
    skips: list[dict[str, str]] = []
    while True:
        ouvrable, motif = est_jour_ouvrable(courant, extras)
        if ouvrable:
            return courant, skips
        skips.append({"date": courant.isoformat(), "motif": motif or "Jour non ouvrable"})
        courant += timedelta(days=1)


def _precedent_jour_ouvrable(
    jour: date,
    fetes_additionnelles: Iterable[date] = (),
) -> tuple[date, list[dict[str, str]]]:
    extras = tuple(fetes_additionnelles)
    courant = jour
    skips: list[dict[str, str]] = []
    while True:
        ouvrable, motif = est_jour_ouvrable(courant, extras)
        if ouvrable:
            return courant, skips
        skips.append({"date": courant.isoformat(), "motif": motif or "Jour non ouvrable"})
        courant -= timedelta(days=1)


def ajuster_ancrage_technologique(
    date_acte: date,
    heure_acte: time | None = None,
    fetes_additionnelles: Iterable[date] = (),
) -> tuple[date, list[str]]:
    """Applique la présomption de l'art. 111 al. 2 C.p.c. à une notification technologique.

    La notification faite par un moyen technologique après 17 h 00, un samedi ou un
    jour férié est réputée faite à 8 h 00 le jour ouvrable qui suit.
    """
    extras = tuple(fetes_additionnelles)
    notes: list[str] = []
    ouvrable, motif = est_jour_ouvrable(date_acte, extras)
    apres_17h = heure_acte is not None and heure_acte > time(17, 0)

    if not ouvrable:
        suivant, _ = _prochain_jour_ouvrable(date_acte + timedelta(days=1), extras)
        notes.append(
            f"Notification technologique faite un jour non ouvrable ({date_acte.isoformat()}, "
            f"{motif}) : réputée faite à 8 h 00 le {suivant.isoformat()} (art. 111 al. 2 C.p.c.)."
        )
        return suivant, notes

    if apres_17h:
        suivant, _ = _prochain_jour_ouvrable(date_acte + timedelta(days=1), extras)
        heure_str = heure_acte.strftime("%H:%M") if heure_acte else ""
        notes.append(
            f"Notification technologique faite à {heure_str} (après 17 h 00) le "
            f"{date_acte.isoformat()} : réputée faite à 8 h 00 le {suivant.isoformat()} "
            "(art. 111 al. 2 C.p.c.)."
        )
        return suivant, notes

    if heure_acte == time(17, 0):
        notes.append(
            "Notification technologique reçue exactement à 17:00 : vérifier la seconde "
            "exacte de réception/transmission au regard de l'art. 111 al. 2 C.p.c. (« après 17 h »)."
        )

    return date_acte, notes


def _ajouter_mois(debut: date, mois_delta: int) -> tuple[date, bool]:
    """Ajoute ou retranche un nombre entier de mois selon l'art. 83 al. 2 C.p.c."""
    total_mois = debut.year * 12 + (debut.month - 1) + mois_delta
    annee, mois_m1 = divmod(total_mois, 12)
    mois = mois_m1 + 1
    dernier_jour = calendar.monthrange(annee, mois)[1]
    quantieme_ajuste = debut.day > dernier_jour
    jour = min(debut.day, dernier_jour)
    return date(annee, mois, jour), quantieme_ajuste


def _dans_periode_non_siege(d: date) -> str | None:
    """Signale si la date tombe dans une période où les tribunaux ne sont pas tenus de siéger."""
    if (d.month == 6 and d.day >= 30) or d.month in (7, 8) or (d.month == 9 and d.day == 1):
        return "du 30 juin au 1er septembre"
    if (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 7):
        return "du 20 décembre au 7 janvier"
    return None


def _avertissement_date_sensible(d: date) -> str | None:
    if (d.month, d.day) == (9, 30):
        return (
            "ATTENTION — 30 septembre : la Journée nationale de la vérité et de la "
            "réconciliation est un jour férié fédéral, mais ne figure ni à l'art. 61 (23°) "
            "de la Loi d'interprétation du Québec (RLRQ, c. I-16) ni à l'art. 82 al. 1 C.p.c. "
            "En procédure civile québécoise, l'échéance n'est pas reportée de plein droit "
            "(vérifier toutefois si le dossier relève d'une loi ou juridiction fédérale)."
        )
    if (d.month, d.day) in ((12, 24), (12, 31)):
        return (
            f"ATTENTION — {d.isoformat()} (veille de fête) : ce jour n'est pas un jour "
            "férié au sens de l'art. 82 al. 1 C.p.c. ni de l'art. 61 (23°) I-16. Vérifier "
            "les heures d'ouverture du greffe (art. 107 al. 4 C.p.c.) et déposer plus tôt "
            "par prudence."
        )
    return None


def calculer_delai(
    ancrage: date,
    valeur: int,
    unite: Literal["jours", "mois"] = "jours",
    sens: Literal["avant", "rebours"] = "avant",
    mode_notification: Literal["ordinaire", "technologique"] = "ordinaire",
    heure_notification: time | None = None,
    fetes_additionnelles: Iterable[date] = (),
) -> dict[str, Any]:
    """Calcule une échéance procédurale selon les art. 82, 83 et 111 al. 2 C.p.c."""
    if valeur < 0:
        raise ValueError("La valeur du délai doit être positive ou nulle.")
    if unite not in ("jours", "mois"):
        raise ValueError(f"Unité invalide : {unite!r} (attendu 'jours' ou 'mois').")
    if sens not in ("avant", "rebours"):
        raise ValueError(f"Sens invalide : {sens!r} (attendu 'avant' ou 'rebours').")

    extras = tuple(fetes_additionnelles)
    avertissements: list[str] = []

    if mode_notification == "technologique":
        ancrage_effectif, notes_ancrage = ajuster_ancrage_technologique(
            ancrage, heure_notification, extras
        )
    else:
        ancrage_effectif, notes_ancrage = ancrage, []
        if heure_notification is not None and heure_notification > time(17, 0):
            notes_ancrage.append(
                "Heure après 17 h 00 fournie en mode ordinaire : noter qu'une signification ou "
                "notification à un avocat, notaire ou huissier hors des heures de l'art. 111 al. 1 "
                "C.p.c. exige le consentement ou soulève une irrégularité."
            )

    delta = valeur if sens == "avant" else -valeur
    quantieme_ajuste = False
    if unite == "jours":
        echeance_brute = ancrage_effectif + timedelta(days=delta)
    else:
        echeance_brute, quantieme_ajuste = _ajouter_mois(ancrage_effectif, delta)

    if sens == "avant":
        echeance, reports = _prochain_jour_ouvrable(echeance_brute, extras)
        echeance_report_suivant = echeance
    else:
        echeance, reports = _precedent_jour_ouvrable(echeance_brute, extras)
        echeance_report_suivant, _ = _prochain_jour_ouvrable(echeance_brute, extras)
        if reports:
            avertissements.append(
                f"Calcul à rebours (« au moins {valeur} {unite} avant ») : l'échéance brute "
                f"({echeance_brute.isoformat()}) tombe un jour non ouvrable; pour préserver "
                f"l'entier délai minimal avant l'événement, l'acte devrait être accompli au plus "
                f"tard le jour ouvrable précédent ({echeance.isoformat()})."
            )

    if quantieme_ajuste:
        avertissements.append(
            f"Ajustement de quantième (art. 83 al. 2 C.p.c.) : le mois d'échéance ne comporte "
            f"pas de quantième {ancrage_effectif.day}, l'échéance brute est ramenée au dernier "
            f"jour du mois ({echeance_brute.isoformat()})."
        )

    non_siege = _dans_periode_non_siege(echeance)
    if non_siege:
        avertissements.append(
            f"Période de non-siège ({non_siege}, art. 82 al. 2 C.p.c.) : les délais continuent "
            "de courir normalement et ne sont pas suspendus."
        )

    for candidat in {echeance_brute, echeance}:
        alerte = _avertissement_date_sensible(candidat)
        if alerte:
            avertissements.append(alerte)

    avertissements.append(
        "Rappel de dépôt (art. 107 al. 4–5 C.p.c.) : le délai expire à 24 h 00 (art. 83 al. 3), "
        "mais un acte sur support technologique transmis après les heures d'ouverture du greffe "
        "est réputé déposé à la prochaine ouverture et doit être accompagné du paiement requis."
    )

    return {
        "ancrage_initial": ancrage.isoformat(),
        "ancrage_effectif": ancrage_effectif.isoformat(),
        "mode_notification": mode_notification,
        "heure_notification": heure_notification.strftime("%H:%M") if heure_notification else None,
        "valeur": valeur,
        "unite": unite,
        "sens": sens,
        "notes_ancrage": notes_ancrage,
        "echeance_brute": echeance_brute.isoformat(),
        "echeance": echeance.isoformat(),
        "echeance_report_suivant": echeance_report_suivant.isoformat(),
        "reportee": bool(reports),
        "reports": reports,
        "avertissements": avertissements,
        "fondements": [
            "art. 82 C.p.c.",
            "art. 83 C.p.c.",
            "art. 107 al. 4–5 C.p.c.",
            "art. 111 al. 2 C.p.c.",
            "art. 61 (23°) Loi d'interprétation (RLRQ, c. I-16)",
        ],
    }


def _parse_date(val: str) -> date:
    try:
        return date.fromisoformat(val)
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Date invalide : {val!r} (format attendu AAAA-MM-JJ)."
        ) from exc


def _parse_heure(val: str) -> time:
    try:
        parts = val.split(":")
        if len(parts) not in (2, 3):
            raise ValueError
        return time(*(int(p) for p in parts))
    except ValueError as exc:
        raise argparse.ArgumentTypeError(
            f"Heure invalide : {val!r} (format attendu HH:MM ou HH:MM:SS)."
        ) from exc


def _format_texte(res: dict[str, Any]) -> str:
    lignes = [
        f"Ancrage initial   : {res['ancrage_initial']}",
        f"Ancrage effectif  : {res['ancrage_effectif']}",
        f"Délai             : {res['valeur']} {res['unite']} ({'à rebours' if res['sens'] == 'rebours' else 'en avant'})",
        f"Échéance brute    : {res['echeance_brute']}",
        f"Échéance retenue  : {res['echeance']}",
    ]
    for note in res["notes_ancrage"]:
        lignes.append(f"  * {note}")
    if res["reports"]:
        lignes.append("Reports appliqués :")
        for rep in res["reports"]:
            lignes.append(f"  - {rep['date']} : {rep['motif']}")
    if res["avertissements"]:
        lignes.append("Avertissements :")
        for av in res["avertissements"]:
            lignes.append(f"  ! {av}")
    return "\n".join(lignes)


def main(argv: list[str] | None = None) -> int:
    _configure_stdio()
    parser = argparse.ArgumentParser(
        description="Calculer une échéance de procédure civile québécoise (art. 82, 83, 111 al. 2 C.p.c.)."
    )
    parser.add_argument("ancrage", type=_parse_date, help="Date d'ancrage (AAAA-MM-JJ).")
    groupe = parser.add_mutually_exclusive_group(required=True)
    groupe.add_argument("--jours", type=int, help="Nombre de jours.")
    groupe.add_argument("--mois", type=int, help="Nombre de mois.")
    parser.add_argument(
        "--a-rebours",
        action="store_true",
        help="Compter à rebours depuis la date d'événement (« au moins X jours avant »).",
    )
    parser.add_argument(
        "--technologique",
        action="store_true",
        help="Appliquer l'art. 111 al. 2 C.p.c. à l'ancrage (notification technologique).",
    )
    parser.add_argument(
        "--heure",
        type=_parse_heure,
        default=None,
        help="Heure de la notification (HH:MM), utile avec --technologique.",
    )
    parser.add_argument(
        "--fete-additionnelle",
        action="append",
        type=_parse_date,
        default=[],
        help="Date additionnelle non ouvrable (AAAA-MM-JJ, répétable) pour proclamation ou fermeture locale.",
    )
    parser.add_argument("--json", action="store_true", help="Afficher le résultat en JSON.")
    args = parser.parse_args(argv)

    unite: Literal["jours", "mois"] = "jours" if args.jours is not None else "mois"
    valeur = args.jours if args.jours is not None else args.mois
    try:
        res = calculer_delai(
            ancrage=args.ancrage,
            valeur=valeur,
            unite=unite,
            sens="rebours" if args.a_rebours else "avant",
            mode_notification="technologique" if args.technologique else "ordinaire",
            heure_notification=args.heure,
            fetes_additionnelles=args.fete_additionnelle,
        )
    except ValueError as exc:
        print(f"Erreur : {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(_format_texte(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
