---
name: analyse-documentaire
description: >-
  Qualifier les documents d'un dossier de litige civil québécois, en lot ou pièce par pièce :
  arrêter la nature, contrôler les mentions, établir le régime de protection; puis, selon le mode,
  résumer une pièce et dire ce qu'elle prouve, dresser le bordereau des pièces et en contrôler la
  cotation, ou tirer d'un lot la chronologie des événements. Utiliser dès qu'il s'agit de classer,
  trier, qualifier ou analyser un document, une pièce, un courriel ou un lot, quel qu'en soit le
  format (.eml, .pdf, .docx, .xlsx, image), même pour un seul; pour savoir si un document est
  privilégié, communicable ou déposé, ou de quel moyen de preuve il relève. Amorces — classe,
  trie, qualifie ces documents, est-ce privilégié, analyse cette pièce, que prouve ce document,
  liste des pièces, bordereau, cotation, chronologie, ligne du temps. En anglais — classify, is
  this privileged, review these exhibits, what does this prove, exhibit list, timeline. Ne pas
  utiliser pour établir une règle de droit, pour rédiger, ni pour calculer un délai.
---

# Analyse documentaire

Dit ce qu'un document **est**, ce qu'il devrait **porter**, qui peut le **voir** et, au besoin, ce
qu'il **prouve**. Elle complète les deux autres compétences du cabinet : `recherche-juridique`
établit le droit, `redaction-juridique` écrit, celle-ci qualifie.

Elle a quatre modes. Tous partent des trois premiers temps de la méthode — nature, mentions,
régime — et divergent ensuite.

| Mode | Quand | Ce qu'il rend |
|---|---|---|
| **Tri** | Plusieurs documents à classer ou vérifier; un document dont on demande seulement la nature ou le régime | Une ligne par document : nature, régime, signalements |
| **Pièce** | Un document à examiner au fond, dans le contexte d'un dossier ou d'une question | Une fiche : résumé, protection, force probante, implications |
| **Bordereau** | Les pièces d'un acte à lister, coter ou contrôler; l'état de communication à établir | La liste des pièces : cote, désignation, date, régime, communiquée ou non — et les écarts de cotation |
| **Chronologie** | Un lot dont il faut tirer la suite des événements | Une ligne par événement daté, avec sa source, ses incertitudes et ses trous |

Le mode se choisit par ce qui est demandé, non par le nombre de fichiers. « Voici les douze pièces
du client, classe-les » est du tri. « Voici le courriel du 14 mars, qu'est-ce qu'il vaut pour
nous? » est une pièce. « Dresse la liste des pièces de la demande » est un bordereau. « Qu'est-ce
qui s'est passé, et dans quel ordre? » est une chronologie. En cas de doute, trier d'abord, puis
proposer le mode qui convient à ce que le tri révèle. Les modes bordereau et chronologie ont chacun
leur fichier : `references/bordereau.md` et `references/chronologie.md`.

## La règle asymétrique

Une erreur qui **sous-estime** la protection peut mener à une divulgation par inadvertance :
manquement professionnel. L'art. 9 de la Charte des droits et libertés de la personne énonce le
**droit** au secret professionnel; le **devoir** de l'avocat vient de l'art. 131 de la Loi sur le
Barreau et de l'art. 60.4 du Code des professions. Une erreur qui la **surestime** fait perdre du temps. **Ces
deux erreurs ne se valent pas.**

- `PUBLIC` ne s'affirme que si le document porte lui-même la marque de son dépôt ou de sa
  cotation. **L'absence d'indice de protection n'est jamais un indice de caractère public.**
- Devant un doute entre deux régimes, retenir **les deux** : la liste est cumulable, et c'est le
  plus élevé qui gouverne.
- Si rien ne peut être établi, le dire. **Ne jamais inventer `PUBLIC` pour combler un vide.**

## La méthode

Trois temps ordonnés, communs aux quatre modes; c'est l'ordre qui fait la valeur.

**1. Qu'est-ce que c'est.** Arrêter la nature et la sous-nature **avant** d'extraire quoi que ce
soit, et dire en une phrase ce qui, dans le document, l'établit. Voir `references/natures.md`.

**2. Que doit-il porter.** N'extraire que les mentions que cette nature commande. Un contrat, un
courriel, une photographie n'ont ni tribunal, ni district judiciaire, ni numéro de dossier de cour
: pour eux, ces champs sont **nuls**, et leur absence n'est pas une lacune. Ne jamais combler un
champ par déduction — l'absence d'une mention attendue est un **signal**, pas un trou à boucher.
Voir `references/mentions.md`.

**3. Quel en est le régime.** Secret professionnel, privilège relatif au litige ou aux règlements,
confidentiel, ou public. Voir `references/protection.md`.

Les trois étages s'alimentent. Un acte de procédure sans numéro de dossier de cour est
probablement un projet non déposé — donc un document qui n'a jamais accédé au caractère public de
l'art. 11 C.p.c., et qui relève du travail préparatoire.

**4. En mode pièce seulement — que vaut-il et que change-t-il.** Voir la section « Le mode pièce »
et `references/force-probante.md`.

## Lire avant de juger

**Ne jamais juger un document sur son nom de fichier.** La règle vaut d'autant plus que la plupart
des provenances ne rendent qu'un nom et des métadonnées.

| Forme | Comment la lire | À savoir |
|---|---|---|
| **Texte, Markdown, CSV, HTML** | Directement | Le texte suffit; attention aux en-têtes tronqués |
| **Courriel (.eml, .msg)** | Extraire d'abord les en-têtes — expéditeur, destinataires, **copies conformes invisibles comprises quand elles figurent**, date, objet, fil —, puis le corps, puis chaque pièce jointe, qui se qualifie **séparément** | L'objet du fil ne qualifie pas la pièce jointe. Un brouillon porte les mêmes horodatages qu'un envoi : rien n'y prouve qu'il a été communiqué. Une chaîne de réponses contient souvent plusieurs auteurs et plusieurs régimes |
| **PDF** | Couche texte d'abord; pour une page sans texte, rasteriser et regarder, lorsque le document est accessible localement | Une page vide au sens du texte n'est **jamais** une page blanche sur papier |
| **Traitement de texte (.docx)** | Texte, mais aussi **commentaires, marques de révision et propriétés** : ils portent l'auteur réel, les dates et parfois la stratégie | Un projet annoté par l'avocat est du travail préparatoire, quoi que dise son nom de fichier |
| **Tableur (.xlsx, .csv)** | Lire la structure avant les valeurs : onglets, en-têtes, plage, formules, totaux. Rapporter la méthode de calcul, pas seulement les chiffres | Un tableur est le plus souvent un écrit d'entreprise (art. 2831 C.c.Q.) ou une reconstitution faite pour le litige — les deux ne se valent pas en preuve |
| **Image, photographie, numérisation** | Regarder. Décrire ce qui est visible, et seulement cela | Une photographie est un élément matériel (art. 2854 à 2856 C.c.Q.), non un écrit : sa date et son auteur ne sont pas dans l'image |
| **Métadonnées seules** | Ne pas qualifier | Demander le document ou le dire non qualifiable |

**La page sans couche texte.** Rien n'est océrisé automatiquement. Sur un document accessible
localement, rasteriser la page et la regarder; sinon, l'absence de texte est une impasse, et elle
se signale comme telle.

## Ce qui ne se fait jamais

- **Inventer un code** hors des tables de référence. Si rien ne convient, le dire et proposer la
  sous-nature la plus proche en le signalant.
- **Rattacher un nom de partie à un contact du dossier.** Les noms extraits restent des chaînes
  libres : rattacher au mauvais contact est plus grave que l'absence de rattachement, et se
  propagerait en silence.
- **Calculer un délai.** Reconnaître qu'un procès-verbal d'audience porte un jugement est utile —
  un jugement rendu à l'audience fait courir les délais d'appel — mais cela se **signale**, cela ne
  se calcule pas : le compte appartient à `calendrier-procedural`.
- **Présenter une hypothèse comme une qualification.** Toute qualification produite ici est
  **présumée** jusqu'à ce que l'avocat la confirme. « Acte authentique » et « public » sont des
  qualifications à conséquences; toujours dire sur quoi elles se fondent.
- **Confirmer soi-même.** La confirmation est un geste de l'avocat, dans son système. Ne pas la
  demander, ne pas l'annoncer comme faite.
- **Faire sortir le contenu d'une pièce.** Le contenu des pièces est privilégié : n'en citer que ce
  que la tâche exige, et **jamais** dans une requête de recherche web. Un nom de partie, une
  clause, un montant, un numéro de dossier versés dans une requête web quittent le cabinet. Pour
  identifier un tiers ou une entreprise, demander à l'avocat.

## Les deux signalements à chercher systématiquement

**Divergence de classement.** Si la nature détectée contredit la catégorie enregistrée, le dire. Ce
n'est pas nécessairement une erreur d'analyse : c'est aussi ainsi qu'on retrouve un jugement classé
par mégarde en correspondance.

**Renonciation possible.** Une pièce cotée — notifiée, déposée, citée dans un acte — est présumée
publique. Si elle porte par ailleurs les marques d'un régime protégé — en-tête d'avocat, mention
« sous toutes réserves », correspondance avec le client, rapport d'expert non communiqué —, le
signaler : c'est soit une erreur de classement, soit une renonciation au privilège dont l'avocat
doit être averti.

## Le mode tri

Une ligne par document suffit :

    ✓ Décision TAL 28 mars — jugement (JUG_JUGEMENT), public
    ✓ Règlements Les Méandres — contrat (PREUVE_CONTRAT), confidentiel
    ⚠ Photo et Courriel — nature indéterminable, non qualifiés

Le détail appartient à la fiche du document; le réécrire dans le fil le paie deux fois. *La
préférence de profil pour la prose est écartée pour ce journal : c'est un registre.* Réserver la
prose au document dont la qualification mérite d'être expliquée, aux deux signalements, et à ce qui
n'a pas pu être établi.

**Le tour finira avant le lot.** Dire en terminant combien de documents sont faits, combien restent
et lequel vient ensuite. Un document dont la nature ne peut être arrêtée se signale et se saute; il
ne se force pas dans la sous-nature la moins improbable.

## Le mode pièce

Quatre rubriques, dans cet ordre. Aucune ne se saute; une rubrique sans matière s'écrit vide et se
dit vide.

**1. Ce que c'est, et ce qu'il dit.** La nature arrêtée et ce qui l'établit, puis un résumé fidèle
: qui, à qui, quand, sur quoi, et le contenu utile. Distinguer ce que le document **énonce** de ce
que son auteur **savait** ou **voulait** — la seconde lecture est une inférence et s'annonce comme
telle. Citer avec parcimonie et exactitude; une citation approximative dans une note se retrouve
plus tard dans une procédure.

**2. Qui peut le voir.** Le régime de protection, sa raison, et ses conséquences pratiques : la
pièce est-elle communicable, est-elle déjà communiquée, sa production emporterait-elle renonciation
sur un ensemble plus large. Signaler toute marque de renonciation possible.

**3. Ce qu'il prouve.** Le moyen de preuve dont il relève (art. 2811 C.c.Q.), la qualification de
l'écrit s'il en est un, la force probante qui en découle, et les obstacles de recevabilité
prévisibles — original ou copie, intégrité d'un document technologique, déclaration d'un tiers,
prohibition de la preuve testimoniale. Voir `references/force-probante.md`. Ce qu'il **ne** prouve
pas mérite autant d'être écrit que ce qu'il prouve.

Terminer la rubrique par le **statut du fait** que la pièce porte, dans le vocabulaire que
`redaction-juridique` attend : **établi** si la pièce a été lue et qu'elle fait preuve de ce fait;
**rapporté** si elle ne fait que le relater — déclaration d'un tiers, résumé, reconstitution;
**absent** si la pièce ne l'établit pas du tout. C'est cette ligne qui décide si une allégation
pourra être ferme ou devra porter un crochet.

**4. Ce qu'il change.** Les conséquences pour le dossier : le fait qu'il établit ou fragilise, son
effet sur la théorie de la cause, ce qu'il ouvre ou ferme comme moyen, ce qu'il faut aller chercher
ensuite, et tout délai qu'il fait courir — **signalé, jamais calculé**. Si la pièce contredit ce
que le dossier porte, le dire ici et au premier plan.

Terminer par ce qui reste incertain et par la vérification qui lèverait l'incertitude.

**Une pièce défavorable s'analyse comme une pièce favorable.** L'analyse qui ne trouve que ce qui
appuie le client est un piège à retardement, et il se déclenche toujours au mauvais moment.

## Les modes bordereau et chronologie

**Le bordereau** liste les pièces d'un acte : cote, désignation, date propre, régime, état de
communication. Il ne décide pas des cotes — l'acte les fixe dans l'ordre de première invocation,
règle que `redaction-juridique` porte —; il les **constate** et en contrôle la continuité. Saut de
numéro, invocation sans cote, cote sans pièce : ses trois signalements. Voir
`references/bordereau.md`.

**La chronologie** tire d'un lot la suite des événements datés, une ligne par événement, rattachée
à la pièce qui l'établit et au statut du fait. Elle distingue le daté par la pièce, le déduit, et
le trou entre deux dates. Voir `references/chronologie.md`.

Ni l'un ni l'autre ne dispense des trois premiers temps : une pièce n'y entre qu'avec sa nature et
son régime, jamais sur son seul nom de fichier.

## Ce qu'il faut du dossier

Le besoin **INVENTAIRE** dit quels documents existent et sous quelle catégorie; le besoin **TEXTE**
donne leur contenu, quand le système l'expose. En mode pièce, le besoin **FICHE** situe le recours
et le forum, le besoin **THÉORIE** dit à quoi la pièce sert ou nuit, et le besoin **PARTIES**
identifie les auteurs et destinataires — sans jamais rattacher un nom extrait à un contact.

Le besoin **VOCABULAIRE** donne les codes qu'un système accepte en écriture; le besoin
**INSCRIPTION** verse la qualification sur le document. Une analyse qui reste dans le fil de la
conversation est une analyse perdue : quand le système connecté permet de l'inscrire, le proposer.

**Sur un lot, la demande est l'instruction.** Quand l'avocat demande d'analyser plusieurs
documents, il n'y a pas à confirmer chaque inscription une à une : un appel d'inscription par
document, avec sa clé d'idempotence, et un rapport à la fin. Sur **un seul** document dont la
nature est douteuse, proposer avant d'inscrire. Cette autorisation ne couvre que l'inscription de
la qualification — rien d'autre.

Comment servir ces besoins dépend du système — c'est l'affaire d'une compétence d'outillage, s'il
en existe une. **Sans système connecté**, ou lorsque le système n'expose pas l'inscription d'une analyse, régime
dégradé : l'analyse vit dans la conversation, et il faut le dire — rien n'est inscrit sur le
document, aucune catégorie ne change, aucun cliquet de protection ne joue. Verser l'analyse en
note au dossier reste possible **sur instruction expresse**, en sachant qu'une note n'est pas une
qualification : elle n'est pas marquée présumée, elle ne se corrige pas depuis la conversation, et
elle ne doit pas porter plus de contenu privilégié que la tâche n'en exige.

## Le périmètre

| À portée | Tentation | Règle |
|---|---|---|
| Calcul de délai | Un procès-verbal portant jugement fait courir l'appel | **Signaler, jamais calculer.** Le calcul appartient à l'avocat ou à `recherche-juridique` |
| Écriture au dossier — fiche, échéance, signification, tâche | Corriger la fiche que le document contredit, inscrire la signification que le procès-verbal établit | **Hors périmètre.** Poser le signalement, proposer l'écriture prête à exécuter, ne pas l'exécuter |
| Recherche web | Identifier un tiers, une entreprise, un expert | **Jamais avec le contenu d'une pièce** |
| Messagerie, stockage, envoi | Transmettre, classer, renommer | **Hors périmètre.** Cette compétence lit |
| Authentification d'une citation, décomposition d'un numéro de cour | — | **Utiles** — section suivante |

La seule écriture que cette compétence propose de son propre chef est l'inscription de la
qualification sur le document analysé. Rien d'autre : ni note, ni champ de dossier, ni tâche, ni
courriel.

Établir une règle de droit relève de `recherche-juridique`; les ancrages cités ici servent à
**nommer** un document, pas à argumenter. Rédiger un texte à partir de la pièce relève de
`redaction-juridique`.

## Ce que les sources de droit ajoutent au tri

La décomposition d'un numéro de dossier de cour (besoin **GREFFE**) en tire le palais, le district,
le tribunal et le type de greffe. C'est ce qui fait apparaître le segment de matière — celui qui
signale un dossier à accès restreint sous l'art. 16 C.p.c. —, et ce qui permet de contrôler un
district ou un tribunal que l'en-tête du document contredit, divergence qui vaut un signalement.
Trois réserves : les valeurs de segment sont une nomenclature locale, à confirmer plutôt qu'à
mémoriser; l'outil lit une table figée à une date, sans interroger aucun registre ni plumitif; et
il n'établit donc ni que le dossier existe, ni qu'il est actif.

L'authentification d'une citation neutre éprouve en un appel un document qui se présente comme un
jugement ou un arrêt. **Confirmée** conforte la nature. **Discordante** ou **introuvable** est un
signalement, non une conclusion : projet de jugement, décision non diffusée, extrait mal recopié,
ou pièce qui n'est pas ce qu'elle annonce. **Indéterminée** ne porte aucun constat — la
vérification n'a pas eu lieu, et elle reste à faire. N'en jamais tirer un dispositif : ces sources
ne rendent que des métadonnées, et la date qu'un résultat de recherche affiche peut être
approximative.

## Contrôle avant remise

1. **Ordre** — la nature a été arrêtée avant toute extraction, et ce qui l'établit est dit.
2. **Mentions** — seules les mentions que la nature commande ont été cherchées; aucune absence n'a
   été comblée par déduction.
3. **Régime** — le régime est établi par une marque du document, jamais par l'absence de marque;
   en cas de doute, les deux régimes sont retenus.
4. **Noms** — aucun nom extrait n'a été rattaché à un contact du dossier.
5. **Confidentialité** — aucun contenu de pièce n'a quitté l'environnement, ni dans une requête
   web, ni autrement.
6. **Statut** — chaque qualification est annoncée comme présumée, et rien n'est présenté comme
   confirmé.
7. **Signalements** — divergence de classement et renonciation possible ont été cherchées, et le
   résultat est écrit même s'il est négatif.
8. **En mode pièce** — les quatre rubriques y sont, y compris ce que la pièce ne prouve pas et ce
   qui reste incertain.
9. **Déontologie** — toute obligation professionnelle que le lot révèle — pièce obtenue d'un tiers,
   communication protégée reçue par erreur, preuve à conserver — est signalée; voir
   `deontologie-professionnelle`.

## Fichiers de référence

À lire au besoin, un à la fois.

- `references/natures.md` — natures et sous-natures : le vocabulaire de classification, avec son
  ancrage légal. À lire dès qu'il faut nommer un document (temps 1).
- `references/mentions.md` — ce que chaque nature doit porter, ce qui n'est qu'un usage constant,
  et les trois cas où une absence est normale. À lire pour le temps 2.
- `references/protection.md` — les régimes de protection, leurs niveaux, leurs fondements et leurs
  réserves. À lire pour le temps 3.
- `references/force-probante.md` — moyens de preuve, qualification de l'écrit, force probante et
  obstacles de recevabilité. À lire en mode pièce, rubrique 3.
- `references/bordereau.md` — la liste des pièces : colonnes, contrôle de la cotation, état de
  communication, gabarit. À lire en mode bordereau.
- `references/chronologie.md` — la suite des événements : ce qu'est un événement, comment le dater,
  comment marquer l'incertitude et les trous, gabarit. À lire en mode chronologie.
