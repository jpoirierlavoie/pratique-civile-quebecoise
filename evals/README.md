# Suite d'évaluation comportementale (`evals/`)

Quatorze scénarios de régression couvrant les cinq compétences du plugin : détection de la
contamination française et de common law, proportionnalité des recherches, statuts de lecture,
rigueur des délais (dont l'ancrage technologique après 17 h 00, le piège du 30 septembre et le
calcul à rebours), garde-fous de rédaction (crochets visibles, solidarité, exécution provisoire,
actes modifiés, distinction `UNDER ALL RESERVES` / `WITHOUT PREJUDICE`), qualification des pièces
(commentaires Word cachés, caviardage / Loi 25, engagements et objections d'interrogatoire
préalable) et déclencheurs déontologiques concrets sans formule générique.

## Fichiers

- `evals/scenarios.json` — les quatorze scénarios de référence, critères d'évaluation et
  assertions déterministes d'outillage.
- `evals/executer_evals.py` — utilitaire autonome en bibliothèque standard Python pour lister les
  scénarios, valider les utilitaires locaux et noter des réponses produites hors ligne.

## Commandes

```powershell
python evals/executer_evals.py --liste
python evals/executer_evals.py --auto-test
python evals/executer_evals.py --reponses chemin/vers/reponses.json
```

L'exécution `--auto-test` est sans effet secondaire (répertoire temporaire détruit aussitôt) et est
vérifiée par l'intégration continue après `python verifier.py`.
