# Les livrables

Trois paliers gradués selon l'enjeu de la question : la **vérification ponctuelle** (question
ciblée ou contrôle de citations), la **fiche** (question de droit d'une page) et la **note de
recherche** (opinion développée sur dossier). La présentation est cartésienne : on sépare les
sources par nature avant de les appliquer aux faits, de sorte que le lecteur voie d'où vient chaque
proposition et puisse en contester une sans démonter le reste.

Le plan d'argumentation ne figure plus ici : il appartient à `redaction-juridique`,
qui en fait le mode 2 de sa note de stratégie. Ce que la recherche lui transmet, ce sont des
autorités vérifiées **avec leur statut de lecture**, jamais des citations nues.

## 1. La structure commune

Suivre cet ordre. Il est civiliste : le texte fonde, la jurisprudence interprète, la doctrine
explique, et l'application vient après.

```
## Question
## Réponse courte
## Préalables
## Législation
## Jurisprudence
## Doctrine
## Application aux faits
## Attaque adverse
## Réserves et vérifications à faire
## Registre des sources
```

**Question** — reformulée en question de droit, pas la demande telle que reçue. S'il y en a
plusieurs, les numéroter et garder l'ordre dans tout le document.

**Réponse courte** — trois à cinq lignes. Ce qu'on répondrait au téléphone. Si la réponse est
incertaine, le dire ici plutôt que de le réserver aux réserves.

**Préalables** — selon le palier (`references/preliminaires.md`) : en note de recherche, grille
complète à quatre rubriques même vides; en fiche, rubriques actives seulement plus le délai
applicable; en vérification ponctuelle, mention uniquement si un piège temporel ou de compétence
mord.

**Législation** — les articles, avec leur numéro, leur objet et la date de consolidation. Citer
le texte lorsqu'il est court et déterminant; le paraphraser sinon. Indiquer quelle version
s'applique quand la question est temporelle.

**Jurisprudence** — chaque décision avec sa citation vérifiée, son tribunal, sa date et **son
statut de lecture** (`Citée`, `Résumée`, `Rapportée`, `Lue (extrait)` ou `Lue (intégrale)`).
Dans un écrit destiné au tribunal, ne jamais fonder une proposition décisive sur une décision qui
n'est au moins au statut `Lue (extrait)` avec `[par. X]` vérifié majoritaire. En fiche ou en
note d'orientation, une décision `Résumée` ou `Rapportée` se présente avec son attribution
exacte : « la fiche annonce que le tribunal a rejeté le moyen d'irrecevabilité », « selon X… »,
et jamais « le tribunal a jugé que ».

**Doctrine** — auteur, titre, source, et ce que l'auteur en dit. Distinguer la doctrine savante
du bulletin de cabinet.

**Application aux faits** — c'est ici, et seulement ici, que les sources rencontrent le dossier.
Si les faits sont incertains, énoncer l'hypothèse retenue et signaler comment la réponse
changerait sous une autre hypothèse.

**Attaque adverse** — le meilleur argument contraire, dans sa version la plus forte, avec les
autorités qui le portent. Systématique.

**Réserves et vérifications à faire** — les pistes non confirmées, les décisions à lire, les
vérifications doctrinales suggérées, les points où l'état du droit est incertain, et ce que le
retard de consolidation laisse en suspens.

**Registre des sources** — tableau final : autorité, statut, provenance, vérification.

| Autorité | Statut | Provenance | Vérifiée |
|---|---|---|---|
| art. 2925 C.c.Q. | Texte officiel | `legislation_get_article`, consolidé au AAAA-MM-JJ | — |
| 2026 QCCS 2659 | Résumée | `jurisprudence_verify_citations` → CONFIRMÉE | oui |
| Bulletin [cabinet], [date] | Doctrine praticienne | Web, liste blanche | s.o. |

## 2. La fiche

Une question, une page. Question, réponse courte, préalables, fondement avec les articles,
autorités avec leur statut, réserves. On saute l'application aux faits quand la question est
abstraite, jamais l'attaque adverse ni le registre.

C'est le format par défaut d'une question posée en passant.

## 3. La note de recherche

La structure complète, développée. C'est le format d'une opinion, d'une analyse de dossier ou
d'une question à plusieurs volets.

Prose plutôt que listes à puces, sauf pour les données structurées, qui vont en tableau.

## 4. La vérification ponctuelle ou de citations

Format court pour deux cas : une question ciblée en passant (article exact, seuil indexé,
définition) ou un texte d'origine douteuse — un mémoire reçu, une recherche produite par une IA,
un bulletin recopié — dont il faut éprouver les autorités. Réponse directe, article consolidé ou
tableau de citations vérifiées, puis signalement seulement si un écueil de prescription ou de
compétence mord.

Analyser d'abord les formes avec `jurisprudence_parse_citation` pour écarter celles qui ne se
résoudront pas, puis vérifier le reste par lots de vingt-cinq avec `jurisprudence_verify_citations`.
Rendre un tableau, et rien d'autre :

| Citation telle qu'annoncée | Intitulé annoncé | Verdict | Ce que la fiche donne réellement |
|---|---|---|---|

Faire suivre de trois lignes au plus : combien de citations ont été éprouvées, combien sont
confirmées, et ce qu'il faut en conclure sur la source.

**Le verdict DISCORDANTE commande une conclusion, pas une note de bas de page.** Une citation
qui existe mais désigne une autre décision que celle annoncée est la signature d'une référence
fabriquée. Une seule suffit à retirer sa fiabilité à l'ensemble du texte : le dire explicitement
et recommander de tout revérifier plutôt que de corriger la ligne fautive.

NON CONSTRUCTIBLE n'est pas un échec — les citations de recueils (R.C.S., R.J.Q., C.A.) et les
identifiants d'éditeurs (J.E., REJB, EYB, AZ) ne se résolvent pas directement. Enchaîner avec
`jurisprudence_find_case` sur le nom des parties avant de conclure. INTROUVABLE n'établit pas
l'inexistence : la couverture a des bornes historiques et la diffusion connaît un délai.

## 5. Destination

**Recherche rattachée à un dossier** → une note au dossier, catégorie « recherche » (besoin
**INSCRIPTION**).

L'ordre est imposé et ne dépend d'aucun système : lire le dossier d'abord — on n'écrit jamais sur
un dossier qu'on n'a pas lu; chercher ensuite si une note porte déjà sur la même question, et la
compléter plutôt que d'en créer une seconde; obtenir la confirmation de l'utilisateur; puis
seulement écrire.

**La mécanique d'écriture appartient à la compétence d'outillage du système connecté** —
plafonds de caractères et scission qu'ils imposent, clé d'idempotence, absence de déduplication,
irréversibilité. La lire avant la première écriture de la session. Sans système connecté, la
recherche vit dans la conversation et il faut le dire : une note qui n'est pas versée n'existe
pas au dossier.

**Ne jamais viser la note qui porte la théorie de la cause** : elle est en lecture seule.

**Recherche générale**, rattachée à aucun dossier → produire le texte dans la conversation.
Ne pas créer de fichier, ne pas créer de note orpheline.

## 6. Deux règles de rédaction

**Calibrer l'affirmation sur la preuve.** « La Cour d'appel a jugé que… [par. X] » suppose une
lecture au statut `Lue (intégrale)` ou `Lue (extrait)` vérifiée majoritaire. « La fiche annonce »,
« selon tel auteur », « sous réserve de lecture » permettent d'exploiter prudemment les
autorités `Résumée` et `Rapportée` dans les échanges de travail et notes internes. Le lecteur
est un avocat : il sait lire un degré de certitude, et il en a besoin.

**Ne pas remplir.** Une note courte et sûre vaut mieux qu'une note longue et molle. En note de
recherche, quand une rubrique obligatoire est vide, écrire qu'elle est vide et pourquoi; en fiche
ou en vérification ponctuelle, omettre les rubriques sans objet plutôt que d'aligner des mentions
vides.

**Remonter ce qui contredit le dossier.** Lorsque la recherche établit que la qualification, le
délai, le point de départ ou le forum inscrits au dossier sont inexacts, cela va en tête du
livrable, sous la réponse courte — pas dans les réserves. Une erreur de qualification produit
presque toujours une erreur de délai, et c'est souvent la seule chose de la note qui appelle une
action le jour même.
