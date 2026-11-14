---
name: redaction-juridique
description: >-
  Rédiger le bloc de contenu de tout écrit civil ou commercial québécois — procédure, contrat,
  entente, quittance, correspondance (mise en demeure, lettre) et note interne (analyse, théorie
  de la cause, plan d'argumentation). S'enchaîne avec recherche-juridique (assises),
  analyse-documentaire (faits et cotes) et calendrier-procedural (délais). Utiliser dès qu'il
  faut rédiger, réviser ou corriger un texte québécois, même un seul paragraphe. Amorces — rédige,
  prépare, ébauche, brouillon, révise, corrige, allégations, conclusions, clause, mise en demeure,
  lettre, note au dossier. En anglais — draft, write, revise, redline, pleading, originating
  application, statement of claim, demand letter, contract clause, memo. Purger les réflexes
  français et de common law. Ne pas utiliser pour établir le droit (recherche-juridique) ni pour
  la mise en forme par gabarit.
---

# Rédaction juridique québécoise

Produit du **texte**, pas des documents : le bloc de contenu qu'un juriste québécois copie ensuite
dans son gabarit. `recherche-juridique` établit le fondement que cette compétence-ci convertit en
texte; `analyse-documentaire` qualifie les pièces qu'elle invoque.

Quatre familles d'écrits, qui n'obéissent pas aux mêmes coutumes. Choisir la bonne famille est la
première décision, et elle commande tout le reste.

## Le principe qui gouverne

**Deux assises, deux défenses.** Un écrit tient sur son assise factuelle (du dossier) et son assise
juridique (de la recherche), tout en repoussant la contamination française et de common law.
Sauter une étape oblige à reprendre le texte au complet.

## Ce que le bloc ne contient pas

Sauf demande expresse : en-tête, pied de page, intitulé de cour ou cartouche, numéro de dossier,
adresses des parties, date, signature, coordonnées du cabinet, avis d'assignation, table des
matières — le gabarit s'en charge.

Aucun balisage Markdown dans les blocs externes destinés à un gabarit (procédure, acte juridique,
correspondance) : intertitres en majuscules sur leur ligne, gras réservé aux cotes de pièces. **En
revanche**, le Markdown structuré est permis — et recommandé — dans les **notes internes**
(`references/notes-internes.md`), sur **demande expresse**, et dans les **notes ou fiches de
mémoire** structurant un dossier.

## La méthode

Trois étapes, ordonnées. Aucune ne se saute : la famille commande la forme, les assises commandent
la matière, et le contrôle de contamination est le seul qui rattrape ce que les deux premières
laissent passer.

### Étape 1 — Identifier la famille, puis lire son fichier

| Famille | Ce qui la caractérise | Fichier à lire |
|---|---|---|
| **Acte de procédure** | Allégations numérotées de faits; le droit ne s'y écrit pas | `references/actes-de-procedure.md` |
| **Acte juridique** | Contrat, entente, transaction, quittance; articles numérotés d'obligations | `references/actes-juridiques.md` |
| **Correspondance** | Mise en demeure, lettre au confrère, au client, au tribunal; prose suivie | `references/correspondance.md` |
| **Note interne** | Analyse, théorie de la cause, plan d'argumentation; les citations y sont exigées | `references/notes-internes.md` |

**Lire le fichier de la famille avant d'écrire la première phrase.** Chaque famille a ses formules
consacrées, ses interdits et ses assises légales, qui ne se déduisent pas des principes généraux :
un acte de procédure et une note d'analyse obéissent à des règles opposées sur la citation du droit.

Deux familles touchées : deux fichiers, deux blocs, jamais un hybride. Famille indéterminable :
demander.

### Étape 2 — Réunir les deux assises

#### 2.1 L'assise factuelle

Les désignations, dates et cotes exactes se puisent dans cet ordre, en indiquant la source :

1. **Le gestionnaire de dossiers, s'il est connecté** — l'interroger avant d'écrire selon le tableau
   « Ce qu'il faut du dossier ».
2. **À défaut, demander à l'utilisateur** les éléments précis manquants (désignation, date, cote,
   montant).
3. **À défaut encore, laisser des crochets apparents**, repris hors du bloc dans le signalement
   final — **jamais de mémoire**.

#### 2.2 Le statut du fait

Une saisie administrative peut être périmée ou fausse; tout fait allégué doit pouvoir être prouvé.

| Statut | Origine | Ce que la rédaction peut en faire |
|---|---|---|
| **Établi** | Pièce lue, document téléversé, aveu, jugement, acte signé | Allégation ferme, avec sa cote de pièce |
| **Rapporté** | Déclaration du client, note au dossier, courriel | Allégation, mais signalée à l'utilisateur comme reposant sur la parole du client |
| **Administratif** | Valeur saisie dans un système — rôle, montants, qualification, date de prescription | Sert à repérer seulement; jamais à alléguer sans vérification |
| **Absent** | Rien au dossier | Crochet visible : [DATE À CONFIRMER], [MONTANT], [COTE], [DÉSIGNATION EXACTE] |

**Ne jamais combler par un fait plausible** : une date inventée se découvre à l'interrogatoire. Le
statut d'un fait tiré d'une pièce vient de `analyse-documentaire` (`../analyse-documentaire/SKILL.md`);
si une échéance procédurale est en jeu, la valider via `calendrier-procedural`
(`../calendrier-procedural/SKILL.md`).

#### 2.3 L'assise juridique

Situer la demande dans l'un de ces trois états, et avertir l'utilisateur hors du premier :

**Fondement établi.** La recherche a été faite dans la conversation ou l'utilisateur fournit les
assises : rédiger.

**Fondement à établir.** Une règle, un délai, un seuil ou une condition reste non vérifié : lire
`../recherche-juridique/SKILL.md` et exécuter la recherche proportionnelle avant de rédiger.

**Fondement volontairement écarté.** L'utilisateur veut un canevas ou une reformulation : rédiger,
et marquer hors du bloc les propositions de droit non vérifiées.

**Aucun numéro d'article ne s'écrit de mémoire.** Le vérifier à la source ou l'omettre.

### Étape 3 — Le contrôle de contamination

Le Québec étant minoritaire dans les corpus francophone (français) et canadien (common law), la
contamination produit des textes dangereux qui imitent la forme du droit applicable.

#### La contamination française

En France, l'acte introductif plaide en droit; au Québec, l'article 99 C.p.c. exige d'énoncer
**les faits**, sans argumenter le droit (« Vu l'article… », « de jurisprudence constante » sont à
supprimer).

| Marqueur français | Correspondance québécoise |
|---|---|
| PAR CES MOTIFS | POUR CES MOTIFS, PLAISE AU TRIBUNAL |
| Assignation, exploit d'huissier | Demande introductive d'instance, avis d'assignation |
| Conclusions (au sens d'écritures), conclusions récapitulatives | Actes de procédure; « conclusions » au Québec = ce qui est demandé au tribunal |
| Référé, ordonnance de référé | Demande en injonction interlocutoire ou provisoire, demande de sauvegarde |
| Tribunal judiciaire, tribunal de commerce, prud'hommes | Cour supérieure, Cour du Québec, Tribunal administratif du travail |
| Pourvoi en cassation, moyen de cassation | Appel, pourvoi à la Cour suprême |
| Mise en état, juge de la mise en état, ordonnance de clôture | Protocole de l'instance, mise en état du dossier, gestion d'instance |
| SARL, SAS, SASU, gérant | Société par actions, inc., ltée, administrateur, dirigeant |
| Articles 1240, 1382, 2224, 1641, 1134 | 1457, 2925, 1726 et suivants, 1434 C.c.Q. |
| Sous huitaine, sous quinzaine | Dans un délai de X jours |
| Conditions générales de vente, CGV, CGU | Conditions générales, modalités |

**Le test de l'article** reste le plus rapide : un numéro d'article français dans un texte
prétendument québécois condamne tout le passage, pas seulement la phrase.

#### La contamination de common law

Plus discrète, parce qu'elle passe souvent par la traduction. Un concept de common law traduit en
français correct reste un concept de common law.

| Réflexe de common law | Ce qu'il faut écrire, ou pourquoi il tombe |
|---|---|
| Énumérer les *grounds* : duty, breach, causation, damages | Alléguer les faits; la qualification suit dans quelques allégations dédiées |
| Duty of care, standard of care | Faute au sens de l'article 1457 C.c.Q.; il n'existe pas de duty of care en droit québécois |
| Consideration, « en contrepartie de la somme de 1 $ » | Le contrat se forme par le seul échange de consentement (art. 1385 C.c.Q.) |
| Tort, tortious | Responsabilité extracontractuelle |
| Statement of claim, motion | Demande introductive d'instance, demande (en anglais : *originating application*, *application*) |
| Pleadings | Actes de procédure — **en anglais**, *pleading* est le terme officiel du C.p.c. (art. 99) |
| Affidavit | Déclaration sous serment — **en anglais**, *affidavit* est le terme officiel du C.p.c. |
| Discovery, examination for discovery | Interrogatoire préalable à l'instruction (*examination on discovery* / *examination* au C.p.c.) |
| Limitation period | Prescription (*prescription* en anglais au C.c.Q.) |
| Specific performance | Exécution en nature — **en anglais**, *specific performance* est le terme officiel du C.c.Q. (art. 1601) |
| Punitive damages réclamés d'office | Ils n'existent que « lorsque la loi prévoit » leur attribution (art. 1621 C.c.Q.) : nommer la loi ou ne pas les réclamer |
| Estoppel | Fin de non-recevoir; la préclusion n'est pas reçue telle quelle |
| Indemnify and hold harmless | Garantir et prendre fait et cause (*indemnify and take up the defence*) |
| Severability / clause de divisibilité importée | La divisibilité est la règle par défaut (art. 1438 C.c.Q.) |
| Without prejudice | *SOUS TOUTES RÉSERVES*; en anglais : *UNDER ALL RESERVES* (réserve de droits) vs *WITHOUT PREJUDICE* (pourparlers); omettre sur une mise en demeure produite |
| Cease and desist letter | Mise en demeure (en anglais : *extrajudicial demand*, art. 1595 C.c.Q., *formal notice* ou *mise en demeure*) |
| Equitable relief, equity | Aucun équivalent; raisonner en droit civil |

**Ce qui n'est pas contaminé.** Les arrêts de la Cour suprême, le droit fédéral et les décisions
québécoises rédigées en anglais sont pleinement applicables. Rédiger en anglais pour un forum
québécois est normal — avec la terminologie officielle, non traduite.

Tables complètes, faux amis et mécanismes : `references/contamination.md` — **obligatoire** pour
réviser un texte dont on soupçonne l'origine, et pour toute rédaction en anglais.

## Ce qu'il faut du dossier

Les besoins à servir avant d'écrire, par ordre d'utilité — à écourter selon la famille. Chaque
fichier de famille précise, à sa section 0, lesquels lui sont indispensables.

| Besoin | Ce qu'il apporte à la rédaction |
|---|---|
| **FICHE** | L'ancrage : qualification, matière, recours, forum, délais, renvois. Une qualification marquée à confirmer est à vérifier aux sources, pas à reprendre telle quelle |
| **PARTIES** | Désignations exactes, forme juridique, identifiants, qualités, coordonnées. Indispensable à LES PARTIES d'un acte de procédure et à l'identification des parties d'un acte juridique |
| **THÉORIE** | La théorie de la cause : c'est précisément ce qu'un acte de procédure doit servir. **Lecture seule; ne jamais chercher à y écrire** |
| **NOTES** | La substance déjà écrite, et le doublon à éviter |
| **INVENTAIRE** | Ce qui existe comme document — donc la cote et la formule de pièce, et le téléversement à demander |
| **CORRESPONDANCE** | Ce que le dossier ne porte pas : l'échange antérieur, les engagements pris, la mise en demeure déjà envoyée |
| **ÉCHÉANCES** | Le contexte procédural, quand l'écrit s'y rattache |
| **CALCUL** | Tout délai de procédure à énoncer, plutôt qu'un calcul à la main |
| **GREFFE** | Le district et le tribunal à alléguer, dérivés du numéro de dossier de cour |

**La substance vit souvent hors du dossier**, dans la correspondance plutôt que dans les notes :
servir le besoin **CORRESPONDANCE** en deux passes, les messages reçus puis les envoyés, et
chercher par nom de partie plutôt que par numéro de dossier.

Comment obtenir ces besoins dépend du système connecté — c'est l'affaire d'une compétence
d'outillage, s'il en existe une pour ce système. Lorsqu'aucun dossier n'existe ou qu'aucun système
ne répond, le dire et travailler avec ce que l'utilisateur fournit. **Ne jamais basculer en silence
sur la mémoire pour combler.**

## La discipline commune aux quatre familles

**Sobriété calibrée.** Couper l'émotivité et l'éditorial (« scandaleux », « outrageux »), jamais la
précision (« dur et acéré », « manifeste »). Un qualificatif survit si son retrait appauvrit les
faits; sinon, couper.

**Une idée cohérente par unité.** Un paragraphe d'allégation ou une clause porte une idée et ses
descripteurs directs; ne scinder qu'au changement de catégorie (faute, préjudice, lien de
causalité).

**Verbes.** Présent pour l'actuel, passé composé pour l'accompli; préférer le verbe exact (« a
constaté », « a fait défaut de donner suite »). Ne pas répéter un point sous trois formes.

**Bilinguisme.** Suivre la langue du dossier, non celle de la demande. En anglais, **ne jamais
traduire un terme de procédure ou de droit civil : le prendre dans la version anglaise officielle
du texte**, par `legislation_get_article(lang="en")` — *originating application*, *case protocol*,
*exhibit*, *extrajudicial demand*, *private writing*. Certains termes que la table de contamination
proscrit en français sont le mot officiel en anglais — *affidavit* pour la déclaration sous
serment, *specific performance* pour l'exécution en nature. Voir la section « Terminologie
anglaise officielle » de `references/contamination.md`.

## Le périmètre

Cette compétence **lit** le dossier; elle n'y écrit pas. Aucune écriture — note, événement, tâche,
signification, événement de prescription — sans demande explicite de l'utilisateur portant sur
cette écriture précise.

Elle n'établit pas le droit : c'est `recherche-juridique`, qui produit la fiche et la note de
recherche. Elle ne qualifie pas les documents ni leur régime de protection : c'est
`analyse-documentaire`. Elle produit en revanche la note d'analyse, la théorie de la cause, le
plan d'argumentation et le plan d'interrogatoire préalable — le plan d'argumentation étant le
document où les citations réapparaissent au grand jour, devant le tribunal.

Elle ne met pas en forme : en-têtes, cartouches et blocs de signature appartiennent aux gabarits.

## Contrôle avant remise

1. **Famille** — le fichier de la famille a été lu, et le texte suit sa structure.
2. **Faits** — chaque fait allégué est établi ou rapporté, sa source est identifiable, aucun
   crochet n'a été comblé par un fait plausible, et les désignations viennent du dossier.
3. **Mise en forme** — un bloc externe destiné à un gabarit est exempt d'en-tête, d'intitulé de
   cour, de bloc de signature, de coordonnées et de tout balisage Markdown; le Markdown reste admis
   dans les notes internes, les fiches de mémoire et sur demande expresse.
4. **Contamination française** — aucun marqueur, aucun numéro d'article français, aucune formule
   d'écriture française.
5. **Contamination de common law** — aucun concept importé, aucune énumération de *grounds*, aucune
   réclamation de dommages punitifs sans loi qui les prévoie.
6. **Droit cité** — dans un acte de procédure ou une correspondance, aucune citation hors des
   exceptions prévues par le fichier de la famille; dans une note interne, chaque proposition de
   droit porte sa source et son statut de lecture.
7. **Numéros vérifiés** — chaque article, seuil et délai a été récupéré à la source pendant cette
   conversation, ou est signalé comme à vérifier.
8. **Sobriété** — relire en cherchant les adjectifs; chacun survit s'il précise, tombe s'il
   amplifie.
9. **Déontologie** — si un fait concret de l'écrit déclenche une obligation (communication avec
   une partie représentée, engagement pris, sincérité envers le tribunal), lire
   `../deontologie-professionnelle/SKILL.md` et la signaler au texte; sans déclencheur concret,
   aucune mention générique.

Signaler à l'utilisateur, **hors du bloc**, ce qui reste à décider ou à vérifier : crochets à
combler, montants à confirmer, pièces à coter, dates à valider, désignations à compléter,
propositions de droit non vérifiées. Ce signalement vit à l'extérieur du texte à copier, jamais
dedans.

## Fichiers de référence

Chacun des quatre fichiers de famille s'ouvre sur une section 0 qui dit ce qu'il faut du dossier
avant d'écrire.

- `references/actes-de-procedure.md` — la famille la plus codifiée : unité d'allégation, formule de
  pièce, allégations de caractérisation, dommages, compétence, conclusions (solidarité et exécution
  provisoire), actes modifiés (art. 206 à 208 C.p.c.) et les variantes.
- `references/actes-juridiques.md` — contrats et actes consensuels : architecture, clauses usuelles,
  et les limites impératives du C.c.Q. qui rendent inopérantes les clauses importées.
- `references/correspondance.md` — mise en demeure et lettres : assises légales de la demeure,
  registre, formules d'appel et de politesse, mentions de réserve.
- `references/notes-internes.md` — note d'analyse, et note de stratégie en trois modes : la théorie
  de la cause, le plan d'argumentation et le plan d'interrogatoire préalable. La famille où les
  citations sont exigées.
- `references/contamination.md` — tables complètes des marqueurs français et de common law, faux
  amis, lexique de substitution, et la **terminologie anglaise officielle** tirée des versions
  anglaises du C.p.c. et du C.c.Q. À lire pour toute révision d'un texte d'origine incertaine et
  pour toute rédaction en anglais.
