---
name: analyse-documentaire
description: >-
  Qualifier les documents d'un dossier de litige civil québécois, en lot ou pièce par pièce :
  nature, mentions, régime de protection, résumé et force probante, bordereau, cotation et
  chronologie. Fournit les faits établis et cotes à redaction-juridique et signale les pièces
  datées à calendrier-procedural. Utiliser dès qu'il faut classer, trier, qualifier ou analyser
  un document (.eml, .pdf, .docx, .xlsx, image), ou vérifier s'il est privilégié ou communicable.
  Amorces — classe, trie, qualifie ces documents, est-ce privilégié, analyse cette pièce, que
  prouve ce document, liste des pièces, bordereau, cotation, chronologie. En anglais — classify,
  is this privileged, review these exhibits, what does this prove, exhibit list, timeline. Ne pas
  utiliser pour établir une règle de droit (recherche-juridique), pour rédiger
  (redaction-juridique), ni pour calculer un délai (calendrier-procedural).
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

Le mode suit la demande, jamais le nombre de fichiers. En cas de doute, trier d'abord puis
proposer le mode adapté; les modes bordereau et chronologie se lisent respectivement dans
`references/bordereau.md` et `references/chronologie.md`.

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

**Inspection technique locale et page sans texte.** Rien n'est océrisé automatiquement. Sur toute
pièce locale (`.docx`, `.xlsx`, `.eml`, `.pdf`, image), exécuter d'abord `scripts/inspecter_piece.py`
(`python scripts/inspecter_piece.py <fichier>`) pour révéler commentaires Word, révisions, formules
et onglets cachés, `Bcc`/`X-Unsent`, chiffrement, `AUCUNE_COUCHE_TEXTE_DETECTEE` ou EXIF. Sur
PDF sans texte, rasteriser et regarder; sinon, signaler l'impasse.

## Ce qui ne se fait jamais

- **Inventer un code** hors des tables; si rien ne convient, proposer la sous-nature la plus proche.
- **Rattacher un nom à un contact du dossier.** Les noms restent des chaînes libres.
- **Calculer un délai.** Un jugement rendu à l'audience fait courir l'appel : le **signaler**,
  renvoyer le calcul à `calendrier-procedural` (`../calendrier-procedural/SKILL.md`).
- **Présenter une hypothèse comme confirmée.** Toute qualification est **présumée** jusqu'à
  confirmation de l'avocat dans son système — ne pas confirmer ni demander confirmation.
- **Faire sortir le contenu d'une pièce.** Le contenu est privilégié : n'en citer que l'essentiel
  et **jamais** dans une requête web; pour identifier un tiers, demander à l'avocat.

## Les trois signalements à chercher systématiquement

**Divergence de classement.** Si la nature détectée contredit la catégorie enregistrée, le dire. Ce
n'est pas nécessairement une erreur d'analyse : c'est aussi ainsi qu'on retrouve un jugement classé
par mégarde en correspondance.

**Renonciation possible.** Une pièce cotée — notifiée, déposée, citée dans un acte — est présumée
publique. Si elle porte par ailleurs les marques d'un régime protégé — en-tête d'avocat, mention
« sous toutes réserves », correspondance avec le client, rapport d'expert non communiqué —, le
signaler : c'est soit une erreur de classement, soit une renonciation au privilège dont l'avocat
doit être averti (sauf partage sous privilège d'intérêt commun, également à signaler).

**Caviardage ou pli cacheté requis.** Avant toute communication ou production au dossier du tribunal,
repérer tout élément d'identification généralement tenu pour confidentiel ou protégé : numéro
d'assurance sociale (NAS), numéro de compte bancaire ou de carte de crédit, mot de passe, dossier
médical ou psychosocial, identité ou coordonnées d'un enfant mineur ou d'une victime (art. 108 al. 1
et 16 C.p.c.; *Loi sur la protection des renseignements personnels dans le secteur privé*, RLRQ,
c. P-39.1), ou secret commercial critique relevant d'une ordonnance sous l'art. 12 C.p.c.

## Le mode tri

Une ligne par document suffit :

    ✓ Décision TAL 28 mars — jugement (JUG_JUGEMENT), public
    ✓ Règlements Les Méandres — contrat (PREUVE_CONTRAT), confidentiel
    ⚠ Photo et Courriel — nature indéterminable, non qualifiés

Le détail appartient à la fiche du document; le réécrire dans le fil le paie deux fois. *La
préférence de profil pour la prose est écartée pour ce journal : c'est un registre.* Réserver la
prose au document dont la qualification mérite d'être expliquée, aux trois signalements, et à ce qui
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

**3. Ce qu'il prouve.** Moyen de preuve (art. 2811 C.c.Q.), force probante et obstacles de
recevabilité (original, intégrité technologique, ouï-dire, preuve testimoniale) selon
`references/force-probante.md`, en précisant aussi ce que la pièce **ne** prouve pas. Clore par le
**statut du fait** pour `redaction-juridique` : **établi** (pièce lue faisant preuve), **rapporté**
(relaté par un tiers/résumé) ou **absent** (non établi).

**4. Ce qu'il change.** Impact sur les faits, la théorie de la cause, les moyens, les vérifications
à suivre et tout délai déclenché (**signalé, jamais calculé**). Toute contradiction avec la fiche
du dossier se met au premier plan, suivie de ce qui reste incertain. Une pièce défavorable s'analyse
avec la même rigueur qu'une pièce favorable. Sur une transcription `TRANS_INTERROGATOIRE`, dresser
systématiquement deux tableaux avec page et ligne : **engagements** souscrits (cote, objet, pièce ou
renseignement promis, état) et **objections** soulevées (art. 228 al. 2 C.p.c., suspensives à
soumettre dans les 5 jours — délai à signaler vers `calendrier-procedural` — par opposition aux
objections non suspensives de l'art. 228 al. 3).

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

Les besoins **INVENTAIRE** (liste et catégorie) et **TEXTE** (contenu) guident tout tri. En mode
pièce s'ajoutent **FICHE** (recours/forum), **THÉORIE** et **PARTIES** (sans jamais rattacher un
nom à un contact).

Les besoins **VOCABULAIRE** et **INSCRIPTION** permettent d'inscrire la qualification présumée au
système connecté. Sur un lot, la demande autorise l'inscription pièce par pièce (avec clé
d'idempotence et rapport final); sur un document unique douteux, proposer d'abord. **Sans système
connecté**, l'analyse vit dans la conversation — le signaler explicitement; une note au dossier
n'est versée que sur instruction expresse, avec le minimum de contenu privilégié.

## Le périmètre

| À portée | Tentation | Règle |
|---|---|---|
| Calcul de délai | Un procès-verbal portant jugement fait courir l'appel | **Signaler, jamais calculer.** Le calcul appartient à l'avocat ou à `calendrier-procedural` (`../calendrier-procedural/SKILL.md`) |
| Écriture au dossier — fiche, échéance, signification, tâche | Corriger la fiche que le document contredit, inscrire la signification que le procès-verbal établit | **Hors périmètre.** Poser le signalement, proposer l'écriture prête à exécuter, ne pas l'exécuter |
| Recherche web | Identifier un tiers, une entreprise, un expert | **Jamais avec le contenu d'une pièce** |
| Messagerie, stockage, envoi | Transmettre, classer, renommer | **Hors périmètre.** Cette compétence lit |
| Authentification d'une citation, décomposition d'un numéro de cour | — | **Utiles** — ci-dessous |

La seule écriture que cette compétence propose de son propre chef est l'inscription de la
qualification sur le document analysé. Rien d'autre : ni note, ni champ de dossier, ni tâche, ni
courriel.

Établir une règle de droit relève de `recherche-juridique` (`../recherche-juridique/SKILL.md`);
les ancrages cités ici servent à **nommer** un document, pas à argumenter. Rédiger un texte à
partir de la pièce relève de `redaction-juridique` (`../redaction-juridique/SKILL.md`).

### Ce que les sources de droit ajoutent au tri

La décomposition d'un numéro de cour (besoin **GREFFE**) extrait palais, district, tribunal et
segment de matière (signalant un accès restreint sous l'art. 16 C.p.c., ou une divergence avec
l'en-tête) sur une table locale figée, sans confirmer que le dossier est actif.

L'authentification d'une citation neutre éprouve un prétendu jugement : **Confirmée** conforte la
nature; **Discordante** ou **introuvable** appelle un signalement (projet, extrait fautif ou pièce
trompeuse); **Indéterminée** laisse la vérification à faire. Ces sources ne rendent que des
métadonnées, jamais un dispositif.

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
7. **Signalements** — divergence de classement, renonciation possible (y compris intérêt commun) et
   besoin de caviardage ou de pli cacheté (art. 108, 12 C.p.c.; Loi 25) ont été cherchés, et le
   résultat est écrit même s'il est négatif.
8. **En mode pièce** — les quatre rubriques y sont, y compris ce que la pièce ne prouve pas et ce
   qui reste incertain.
9. **Déontologie** — uniquement si une pièce révèle un déclencheur concret (pièce obtenue d'un
   tiers, communication privilégiée reçue par erreur, preuve à conserver), lire
   `../deontologie-professionnelle/SKILL.md` et signaler l'obligation au texte; sans déclencheur
   concret, aucune mention générique.

## Fichiers de référence et outillage local

À lire au besoin, un à la fois.

- `scripts/inspecter_piece.py` — utilitaire local autonome en bibliothèque standard Python pour
  inspecter métadonnées, commentaires, marques de révision, formules/onglets cachés, en-têtes de
  courriel et couche texte PDF de pièces locales avant de les qualifier (`--json` pris en charge).

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
