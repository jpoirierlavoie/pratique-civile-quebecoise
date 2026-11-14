---
name: recherche-juridique
description: >-
  Recherche juridique et doctrinale québécoise en droit civil et commercial. Utiliser dès qu'une
  question de droit québécois se pose — règle applicable, délai ou prescription, fondement d'un
  recours, conditions d'ouverture, jurisprudence ou doctrine, moyens préliminaires, validité d'un
  contrat, compétence —, même sans demande explicite. Précède redaction-juridique pour poser ses
  assises et renvoie les délais d'instance à calendrier-procedural. Amorces — quelle est la règle,
  est-ce prescrit, quel délai, sur quel fondement, y a-t-il de la jurisprudence, vérifie ces
  citations. En anglais — legal research, case law, limitation period, prescription, what is the
  rule on, is there authority for. Ne pas utiliser pour rédiger, pour calculer un délai de
  procédure (calendrier-procedural), ni pour qualifier un document (analyse-documentaire).
---

# Recherche juridique québécoise

Établit le fondement, les conditions d'ouverture, les délais et les pièges procéduraux d'une
question de droit civil ou commercial québécois. `redaction-juridique` occupe ensuite le terrain
ainsi préparé; cette compétence-ci sert aussi seule, pour une opinion ou une fiche.

## Le principe qui gouverne

**Une proposition de droit n'est affirmée que si sa source a été rapportée par une source
primaire ou par l'utilisateur.** Le web sert à comprendre et à repérer; il n'autorise jamais. Une
piste trouvée sur le web reste une piste tant qu'elle n'est pas confirmée, et figure au livrable
sous « à vérifier ».

Ce n'est pas une règle de prudence, mais une conséquence de l'outillage disponible : la section
suivante explique pourquoi.

## Ce que l'outillage permet, et ce qu'il interdit

Deux rôles, aux capacités opposées. Ces limites déterminent la méthode; les ignorer produit le
sinistre que la compétence existe pour prévenir — une note élégante, des citations réelles, et un
ratio inventé.

| | Source législative | Source jurisprudentielle |
|---|---|---|
| Texte intégral | **Oui**, verbatim, à la consolidation courante | **Non.** Jamais |
| Recherche par le contenu | **Oui**, plein texte | **Non** |
| Repérage par matière | Oui, taxonomie de matières | Aucun mécanisme fiable |
| Versions antérieures | **Non** | Sans objet |
| Ce qu'elle fait bien | Donner le texte officiel et sa place dans la loi | Authentifier une citation, parcourir le graphe |

**Le corpus législatif est une sélection fermée.** Il porte le Québec et le fédéral, sans
jurisprudence, versions antérieures ni ancien C.p.c. (c. C-25). **Une absence de résultat signifie
que le texte n'est pas dans ce corpus, jamais qu'aucune règle n'existe** — le formuler ainsi.

**La source jurisprudentielle ne cherche pas par sujet.** Elle authentifie une citation, liste
les décisions d'un tribunal entre deux dates, retrouve par nom des parties et parcourt le graphe des
citations depuis un ancrage issu de la doctrine, du dossier ou de l'utilisateur.

**Le texte des jugements est inaccessible.** La récupération automatisée depuis les hyperliens est
bloquée (ni SOQUIJ ni CAIJ) : pour obtenir le texte d'une décision, **demander à l'utilisateur de
la téléverser**, sans contourner en recopiant un corpus.

**Aucune source primaire connectée (régime dégradé).** Le dire d'emblée, travailler sur les textes
fournis par l'utilisateur et marquer *toute* proposition de droit comme non vérifiée, sans jamais
réciter un article de mémoire.

*Les deux rôles sont tenus par des connecteurs distincts, que ce plugin déclare : « Legislation »
(`legislation_*`) pour le texte officiel des lois et des règlements du Québec et du fédéral,
« Jurisprudence » (`jurisprudence_*`) pour l'authentification des décisions. Ce dernier porte aussi
`greffe_*` et `palais_*`, qui n'appellent rien : ils lisent des tables locales du 15 juillet 2026,
à revérifier auprès du Ministère avant toute signification ou tout dépôt. Leur usage détaillé est
dans `references/methode-sources.md`.*

## La méthode

**1. Établir l'appui factuel**, dans l'ordre de préférence de la section « Ce qu'il faut du
dossier ». Ce qu'un dossier porte oriente la recherche; cela ne prouve rien.

**2. Trancher l'urgence avant le fond.** Si une échéance est rapprochée — délai de réponse, dépôt
du protocole, délai de rigueur de mise en état, alerte de prescription —, la question du délai se
traite et se répond **en premier**, quitte à livrer une réponse partielle sur le fond. Une analyse
impeccable remise après l'échéance ne vaut rien. Le dire dès que l'échéance apparaît, sans
attendre la fin de la recherche. Le compte et la qualification d'un délai de procédure relèvent de
`calendrier-procedural` (lire `../calendrier-procedural/SKILL.md`); la prescription reste ici.

**3. Décomposer la demande en questions de droit recherchables.** « Est-ce qu'on peut
poursuivre? » se décompose : quelle est la qualification du rapport de droit, quelle norme le
régit, quelles sont les conditions d'ouverture, quels moyens de défense existent, quelle
réparation est possible, devant quel forum, dans quel délai. Sans cette décomposition, la
recherche part dans le vide.

**4. Passer les préalables selon le palier** — proportionnel à la demande, en s'appuyant sur
`references/preliminaires.md` :

- **Vérification ponctuelle** (article précis, citation douteuse, définition isolée) : contrôler
  mentalement les pièges de prescription ou de compétence; n'écrire un préalable que si un risque
  mord, et répondre directement.
- **Fiche** (question de droit complète ou en cours de dossier) : vérifier les quatre rubriques et
  n'écrire de façon compacte que celles qui s'appliquent (plus le délai de prescription si pertinent).
- **Note de recherche** (opinion développée, analyse de dossier avant procédure) : exécuter et
  écrire intégralement la grille à quatre rubriques, même quand une rubrique est vide.

**5. Établir le texte législatif.** Cadrer par matière, situer dans la structure de la loi, puis
lire l'article. Chercher en plein texte quand on cherche une notion sans savoir où elle loge.
**Toujours relever la date de consolidation** et la reporter dans le livrable.

**6. Lire la doctrine.** Recherche web restreinte aux sources de
`references/sources-doctrinales.md`. Elle sert à deux choses : comprendre la règle, et repérer les
autorités à vérifier ensuite. Citable comme doctrine, jamais comme substitut au texte.

**7. Vérifier la jurisprudence.** Les candidats viennent de l'étape 6, du dossier ou de
l'utilisateur. Pour chacun : authentifier la citation, puis lire la fiche et ses mots-clés — un
digest indexé qui nomme souvent les articles en jeu et les arrêts de principe discutés, donc une
nouvelle moisson de candidats. Étendre par le graphe des citations, vers la postérité et vers les
arrêts de principe. C'est la méthode de la boule de neige, et c'est la seule qui fonctionne ici.

**8. Éprouver la postérité.** L'historique subséquent donne un indice, pas une réponse : il ne
détecte ni l'infirmation, ni les pourvois pendants, ni les refus de permission d'appeler, ni les
désistements. Le signaler comme tel plutôt que de le présenter comme une vérification.

**9. Demander les textes déterminants.** Si le sens exact d'une décision commande la réponse, ne
pas deviner — demander le téléversement.

**10. Chercher l'attaque adverse** — systématique, jamais optionnelle.

**11. Livrer**, selon `references/livrables.md` en choisissant le palier adapté (vérification
ponctuelle, fiche ou note de recherche); si une rédaction suit, transmettre les autorités et leurs
statuts à `redaction-juridique` (lire `../redaction-juridique/SKILL.md`).

## Le statut de lecture

Chaque autorité porte un statut, et ce statut détermine ce que le livrable peut en tirer. La règle
existe parce que le mode d'échec le plus dangereux consiste à lire un intitulé, des mots-clés et
un résumé, puis à écrire « la Cour d'appel a jugé que… ». La citation est réelle, la vérification
superficielle passe, et le ratio est fabriqué.

| Statut | Ce qui est établi | Ce que le livrable peut en dire |
|---|---|---|
| **Citée** | La citation est authentifiée | Nommer la décision, son tribunal, sa date; signaler qu'elle porte sur la question |
| **Résumée** | En sus, la fiche et les mots-clés | Indiquer l'objet et le sens du dispositif tel que le résumé l'annonce, en l'attribuant au résumé |
| **Rapportée** | Ce qu'une source doctrinale identifiée en dit | Rapporter la lecture de l'auteur, en la lui attribuant nommément — jamais comme l'énoncé de la cour |
| **Lue (extrait)** | Extrait textuel exact fourni ou obtenu pour le point précis | Citer le passage avec renvoi au paragraphe (`[par. X]`) après avoir vérifié qu'il exprime la **majorité** et non une dissidence ou un *obiter* isolé |
| **Lue (intégrale)** | Texte intégral lu dans la conversation | Énoncer le ratio, citer avec `[par. X]`, fonder une argumentation écrite devant le tribunal |

**Seuil distinct selon l'usage :**

- **Écrit ou argumentation destiné au tribunal** (plan d'argumentation, cahier d'autorités, avis
  formel) : **aucune proposition décisive ne repose sur une autorité au-dessous de
  « Lue (extrait) » vérifiée majoritaire au `[par. X]`** — et privilégier « Lue (intégrale) ».
- **Échanges de travail et notes internes d'exploration** (`Vérification ponctuelle`, `Fiche`,
  orientation préliminaire) : les statuts `Résumée` et `Rapportée` peuvent orienter l'analyse **à
  la condition expresse** de calibrer la phrase sur la preuve (« la fiche annonce… », « selon tel
  auteur… », « sous réserve de lecture ») et de figurer au registre avec leur statut.

**Le statut voyage avec l'autorité**, y compris dans ce que `redaction-juridique` en fera ensuite.
Il est déterminant au plan d'argumentation, puisqu'une décision non lue y serait citée à un juge.

Une citation **discordante** — elle existe mais renvoie à une autre décision que celle annoncée —
est la signature d'une référence produite par une IA ou recopiée sans vérification. Le signaler
explicitement, et écarter la source qui l'a produite.

## Écarter la France, systématiquement

Le web francophone juridique est dominé par la France. Le vocabulaire est presque identique et le
droit ne l'est pas : une source française sur le vice caché, la prescription ou la responsabilité
est activement dangereuse, parce qu'elle se lit comme du droit applicable.

**Exclure** : tout domaine `.fr`, Légifrance, Dalloz, Village de la Justice, doctrine.fr,
actu-juridique, LexisNexis France, Éditions Législatives, service-public.fr, Cour de cassation,
Conseil d'État. Écarter de même la Belgique, la Suisse et le Luxembourg.

**Le numéro d'article est le test le plus rapide.** Responsabilité délictuelle sous les articles
1240 ou 1382, prescription sous 2224, vices cachés sous 1641 : la source est française et elle est
écartée **entièrement**, pas seulement le passage. Une source qui se trompe de système ne devient
pas fiable sur le reste. Au Québec : 1457, 2925, 1726 et suivants C.c.Q.

Autres marqueurs : pourvoi en cassation, référé, tribunal judiciaire, prud'hommes, SARL,
assignation, PAR CES MOTIFS.

Le droit canadien de common law n'est pas à écarter mais à qualifier : une discussion ontarienne
d'une *limitation period* ne transpose pas. Les arrêts de la Cour suprême et le droit fédéral
demeurent pertinents.

*En recherche, un marqueur écarte la source. En rédaction, un marqueur déclenche une réécriture.
Ce sont deux règles différentes; `redaction-juridique` porte la seconde.*

## Le budget : l'autorité idéale, pas le ratissage

Une recherche québécoise réussie tient en trois à cinq autorités vérifiées : l'article au bon
alinéa, un énoncé de principe (Cour d'appel de préférence), une ou deux applications proches et
l'autorité contraire la plus embêtante. **Zéro décision est parfois le bon résultat** : s'appuyer
alors honnêtement sur la loi et la doctrine plutôt que de remplir avec des citations douteuses.
Écrire au fur et à mesure.

## Demander les jugements à l'utilisateur

C'est la voie directe vers les statuts « Lue (extrait) » et « Lue (intégrale) », et elle est
explicitement ouverte.

Demander de façon directe et parcimonieuse : nommer 1 à 3 décisions vérifiées, leur intérêt et ce
qu'on y cherche, sans attendre la fin de la recherche (vérifier d'abord le besoin **INVENTAIRE**
si la décision est déjà au dossier).

> Trois décisions changeraient la réponse. Pourriez-vous téléverser 2026 QCCA 412 — j'y cherche
> l'énoncé du critère — et 2025 QCCS 3187, pour voir comment le tribunal a traité le point de
> départ du délai sur des faits voisins?

Si le texte ne peut être fourni, le dire : le ratio demeure sous réserve de lecture, et l'analyse
s'appuie sur la loi et la doctrine.

## L'attaque adverse

Systématique. Une recherche qui ne trouve que ce qui appuie la position du client est un piège à
retardement.

Chercher activement l'autorité contraire, formuler le meilleur argument adverse dans sa version la
plus forte, et signaler quand l'état du droit est incertain plutôt que de trancher. Signaler aussi
l'autorité défavorable qui lie le tribunal, même — surtout — quand elle dérange.

## Ce qu'il faut du dossier

**Une question de droit se répond le plus souvent sans aucun fait de dossier.** Quand elle en
exige — un point de départ, une date de signification, une désignation exacte, le forum saisi —,
les obtenir dans cet ordre de préférence, et dire lequel a servi.

**1. Le gestionnaire de dossiers, s'il y en a un de connecté.** C'est la voie la plus rapide, et la
seule qui rende les désignations et les dates telles qu'elles sont inscrites. Les besoins à servir :
**FICHE** pour la qualification, le forum et les délais; **ÉCHÉANCES** pour l'urgence; **THÉORIE**
pour la position déjà arrêtée; **NOTES** pour ce qui a déjà été cherché; **INVENTAIRE** pour savoir
ce qui est déjà versé, et **TEXTE** pour le lire; **CALCUL** pour un délai de procédure; **GREFFE**
pour contrôler un forum; **INSCRIPTION** pour verser le livrable. Comment les obtenir dépend du
système : c'est l'affaire d'une compétence d'outillage, s'il en existe une.

**Rien de ce qu'un tel système rend n'est un fait prouvé.** Ce sont des saisies, faites un jour par
quelqu'un : elles orientent, elles n'établissent pas. Une date de prescription inscrite est un
signal, pas la date pour agir; une qualification inscrite peut dater de l'ouverture et non du
recours réellement exercé.

**2. À défaut, demander à l'avocat.** Nommer les faits qui manquent et dire ce que chacun
changerait à la réponse. Demander peu et demander précisément : une question dont la réponse ne
déplacerait rien ne se pose pas. C'est aussi la voie normale pour le besoin **CORRESPONDANCE**,
qu'aucun dossier ne porte.

**3. À défaut encore, répondre en droit, et le dire.** Une réponse sans appui factuel reste utile —
la règle, ses conditions d'ouverture, le délai et son point de départ théorique — à condition
d'énoncer les hypothèses retenues et de nommer le fait qui les renverserait. **Ne jamais combler un
fait manquant par une supposition vraisemblable :** un crochet visible vaut mieux qu'une date
plausible.

**Quand la recherche contredit ce que le dossier porte**, le dire au premier plan du livrable, pas
dans les réserves. Nommer ce qui y figure, ce qui devrait y figurer, et la conséquence pratique —
une erreur de qualification produit presque toujours une erreur de délai. Ne rien corriger de sa
propre initiative : proposer la correction et laisser l'avocat décider.

## Le périmètre

Cette compétence **lit** le dossier. Elle n'y écrit pas de sa propre initiative : aucune note,
aucun événement de prescription, aucune correction de fiche sans une demande de l'utilisateur
portant sur cette écriture précise.

Elle ne rédige pas d'écrit destiné au tribunal, à une partie ou au client — cela relève de
`redaction-juridique` (`../redaction-juridique/SKILL.md`), qui **supprime les citations du corps
des procédures et des lettres** parce que les articles s'argumentent à l'audience et non dans la
demande. Les citations vivent donc ici, et c'est ici qu'on les retrouvera : la fiche et la note de
recherche portent tout l'appareil que les écrits n'emportent pas. Elle ne qualifie pas les
documents du dossier — cela relève de `analyse-documentaire` (`../analyse-documentaire/SKILL.md`).
Le partage est net : la fiche et la note de recherche sont produites ici; la note d'analyse, la
théorie de la cause et le plan d'argumentation le sont là-bas.

Elle ne verse **jamais** le contenu d'une pièce dans une requête web. Un nom de partie, une
clause, un montant, un numéro de dossier versés dans une recherche web quittent le cabinet.

## Contrôle avant remise

1. **Préalables** — le contrôle préalable a été mené et restitué selon le palier retenu
   (vérification ponctuelle, fiche ou note de recherche complète).
2. **Législation** — chaque article a été lu au texte, avec sa date de consolidation reportée.
3. **Statuts** — chaque autorité porte son statut exact (`Citée`, `Résumée`, `Rapportée`,
   `Lue (extrait)` ou `Lue (intégrale)`) avec `[par. X]` vérifié majoritaire si citée en appui,
   et les autorités non lues restent attribuées à leur résumé ou auteur.
4. **Contamination** — aucune source française, belge, suisse ou luxembourgeoise; aucun numéro
   d'article étranger.
5. **Attaque adverse** — la meilleure position adverse est formulée (sur fiche et note de recherche),
   avec l'autorité contraire nommée.
6. **Réserves** — ce qui n'a pas pu être vérifié est écrit comme tel, jamais omis.
7. **Divergences** — tout ce que la recherche contredit dans la fiche du dossier figure au premier
   plan du livrable, pas dans les réserves.
8. **Chiffres** — seuils de compétence, délais et montants repris d'ailleurs, y compris d'une autre
   compétence, sont des **hypothèses** et non des acquis : ils dérivent avec les modifications
   législatives et ont été revérifiés à la source avant d'être employés.
9. **Déontologie** — uniquement en présence d'un déclencheur concret (conflit, confidentialité,
   délai échu par erreur de l'avocat), lire `../deontologie-professionnelle/SKILL.md` et signaler
   l'obligation au texte; sans déclencheur, aucune mention générique.

## Fichiers de référence

- `references/preliminaires.md` — la grille des préalables et ses ancrages vérifiés. À lire à
  chaque question de fond, c'est-à-dire presque toujours.
- `references/methode-sources.md` — formulation des requêtes, usage détaillé des sources primaires,
  vérification et parcours du graphe. À lire à la première recherche de la session.
- `references/sources-doctrinales.md` — la liste blanche québécoise, ce qui est réellement
  atteignable, et la procédure d'exclusion. À lire avant toute recherche web.
- `references/livrables.md` — les trois gabarits de sortie. À lire au moment de rédiger.
