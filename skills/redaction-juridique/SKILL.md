---
name: redaction-juridique
description: >-
  Rédiger le bloc de contenu de tout écrit juridique québécois en droit civil et commercial — acte
  de procédure, acte juridique (contrat, entente, transaction, quittance), correspondance (mise en
  demeure, lettre au confrère, au client, au tribunal) et note interne (analyse, théorie de la
  cause, plan d'argumentation). Utiliser dès qu'il faut produire, réviser, reformuler ou corriger
  un texte juridique destiné à un dossier québécois, même sans le mot « rédiger », même pour un
  seul paragraphe. Amorces — rédige, prépare, ébauche, projet de, brouillon, révise, corrige,
  allégations, conclusions, clause, mise en demeure, lettre, note au dossier. En anglais — draft,
  write, revise, redline, pleading, statement of claim, demand letter, contract clause, memo.
  Utiliser surtout pour purger un texte de ses réflexes français ou de common law. Seuil
  volontairement bas. Ne pas utiliser pour établir le fondement juridique, qui relève de
  recherche-juridique, ni pour la mise en forme, qui relève des gabarits.
---

# Rédaction juridique québécoise

Produit du **texte**, pas des documents : le bloc de contenu qu'un juriste québécois copie ensuite
dans son gabarit. `recherche-juridique` établit le fondement que cette compétence-ci convertit en
texte; `analyse-documentaire` qualifie les pièces qu'elle invoque.

Quatre familles d'écrits, qui n'obéissent pas aux mêmes coutumes. Choisir la bonne famille est la
première décision, et elle commande tout le reste.

## Le principe qui gouverne

**Un écrit juridique repose sur deux assises et se défend contre deux contaminations.** L'assise
factuelle vient du dossier, l'assise juridique vient de la recherche; la contamination française et
celle de common law déforment la langue même quand les deux assises tiennent. Un texte qui manque
l'une des quatre se reprend au complet — c'est pourquoi la méthode les traite dans cet ordre, et
pourquoi le contrôle final les revérifie une à une.

## Ce que le bloc ne contient pas

Sauf demande expresse : en-tête, pied de page, intitulé de cour ou cartouche, numéro de dossier,
bloc d'adresses des parties, date et lieu de signature, bloc de signature, coordonnées du cabinet,
avis d'assignation, page de présentation, table des matières. Le gabarit s'en charge.

Aucun balisage Markdown non plus : ni titres `#`, ni listes à puces, ni blocs de code. Les
intertitres conventionnels s'écrivent en majuscules sur leur propre ligne. Le gras ne sert qu'aux
cotes de pièces, où la convention l'exige.

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

Une assise factuelle, qui vient du dossier; une assise juridique, qui vient de la recherche. Un
texte qui tient sur une seule des deux se reprend au complet.

#### 2.1 L'assise factuelle

Un écrit juridique tient sur des désignations et des dates exactes, et ce que l'utilisateur dicte
de mémoire est un résumé : un résumé n'a ni les désignations, ni les dates, ni les cotes. Les
obtenir dans cet ordre de préférence, et dire lequel a servi.

**1. Le gestionnaire de dossiers, s'il y en a un de connecté.** L'interroger avant d'écrire,
systématiquement, et ne pas demander à l'utilisateur ce que le dossier détient. Les besoins sont au
tableau de la section « Ce qu'il faut du dossier ».

**2. À défaut, demander à l'utilisateur.** Nommer chaque élément manquant — désignation, date,
cote, montant — plutôt que de demander « les faits ».

**3. À défaut encore, rédiger avec des crochets apparents**, et les reprendre hors du bloc dans le
signalement final. **Ne jamais basculer en silence sur la mémoire pour combler.**

#### 2.2 Le statut du fait

Une valeur saisie dans un système n'est pas un fait prouvé : elle peut être périmée, incomplète ou
fausse — un rôle inversé, une date de prescription qui ignore une interruption. Un acte de
procédure allègue des faits qu'un témoin devra confirmer et qu'une pièce devra soutenir.

| Statut | Origine | Ce que la rédaction peut en faire |
|---|---|---|
| **Établi** | Pièce lue, document téléversé, aveu, jugement, acte signé | Allégation ferme, avec sa cote de pièce |
| **Rapporté** | Déclaration du client, note au dossier, courriel | Allégation, mais signalée à l'utilisateur comme reposant sur la parole du client |
| **Administratif** | Valeur saisie dans un système de gestion — rôle, montants, qualification, date de prescription | Rien. Sert à orienter, nommer et repérer; jamais à alléguer sans vérification |
| **Absent** | Rien au dossier | Un crochet visible dans le brouillon |

**La dernière ligne est celle qui compte.** Quand un fait manque, laisser un crochet apparent —
[DATE À CONFIRMER], [MONTANT], [COTE], [DÉSIGNATION EXACTE] — et le reprendre hors du bloc dans le
signalement final. **Ne jamais combler par un fait plausible.** Une date vraisemblable inventée
dans une allégation ne se voit pas à la relecture; elle se découvre à l'interrogatoire.

Le statut d'un fait tiré d'une pièce vient de `analyse-documentaire` : une pièce lue et qualifiée
porte un fait **établi**; une pièce dont on ne connaît que le nom de fichier n'en porte aucun.

#### 2.3 L'assise juridique

Cette compétence peut être invoquée après `recherche-juridique`, mais rien ne le garantit. Se
situer dans l'un des trois états, et le dire à l'utilisateur si ce n'est pas le premier.

**Fondement établi.** La recherche a été faite dans la conversation, ou l'utilisateur fournit les
assises. Rédiger.

**Fondement à établir.** La rédaction suppose une règle, un délai, un seuil de compétence ou une
condition d'ouverture non vérifiée. Invoquer `recherche-juridique` d'abord. C'est le cas ordinaire
d'une demande reçue à froid, et sauter l'étape est exactement ce qui produit une procédure fondée
sur un article inventé.

**Fondement volontairement écarté.** L'utilisateur veut un brouillon, un canevas, une
reformulation. Rédiger, mais marquer en fin de bloc chaque endroit où le texte repose sur une
proposition de droit non vérifiée.

**Aucun numéro d'article ne s'écrit de mémoire, dans aucune des quatre familles.** Un numéro récité
est indistinguable d'un numéro inventé, et le lecteur ne peut pas faire la différence. Le vérifier
à la source, ou l'omettre.

### Étape 3 — Le contrôle de contamination

C'est le mode d'échec dominant, et il est structurel plutôt qu'accidentel. Le corpus juridique
francophone est massivement français; le corpus juridique canadien est massivement de common law.
Le Québec est minoritaire dans les deux, et son vocabulaire coïncide presque parfaitement avec
celui de la France tout en recouvrant un droit différent. Un texte contaminé se lit donc comme du
droit applicable : c'est précisément ce qui le rend dangereux.

#### La contamination française

**La racine du problème.** En France, l'acte introductif expose les moyens **en fait et en droit**
: il cite les articles, discute la jurisprudence, développe le syllogisme. C'est la forme normale
là-bas. Au Québec, l'article 99 C.p.c. exige que l'acte de procédure « énonce les faits qui le
justifient ». Les faits, et non les moyens de droit. Le tribunal est présumé connaître la loi;
l'argumentation appartient à l'audience et au plan d'argumentation.

Toute pulsion d'écrire « Vu l'article… », « aux termes de l'article… », « conformément aux
dispositions de l'article 1457 C.c.Q. » ou « il est de jurisprudence constante que » dans un acte
de procédure est la signature de ce réflexe. La supprimer.

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
| Statement of claim, pleadings, motion | Demande introductive d'instance, actes de procédure, demande |
| Affidavit | Déclaration sous serment — **en anglais**, *affidavit* est le terme officiel du C.p.c. |
| Discovery, examination for discovery | Interrogatoire préalable à l'instruction |
| Limitation period | Prescription |
| Specific performance | Exécution en nature — **en anglais**, *specific performance* est le terme officiel du C.c.Q. |
| Punitive damages réclamés d'office | Ils n'existent que « lorsque la loi prévoit » leur attribution (art. 1621 C.c.Q.) : nommer la loi ou ne pas les réclamer |
| Estoppel | Fin de non-recevoir; la préclusion n'est pas reçue telle quelle |
| Indemnify and hold harmless | Garantir et prendre fait et cause |
| Severability / clause de divisibilité importée | La divisibilité est la règle par défaut (art. 1438 C.c.Q.) |
| Without prejudice | Sous toutes réserves |
| Cease and desist letter | Mise en demeure |
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

**Sobriété calibrée, jamais télégraphique.** La rédaction québécoise est sobre; elle n'est pas
dépouillée. Retirer le volume émotif et le commentaire éditorial, non la précision. « dur et acéré »,
« avec force », « sur-le-champ », « manifeste » caractérisent un fait de manière contestable — ils
restent. « Scandaleux », « outrageux », « totalement inacceptable », « deeply troubling » tranchent
une question que le tribunal n'a pas tranchée — ils partent, sans exception. Le test : si le retrait
change ce qu'un lecteur raisonnable comprend, garder; sinon, couper. En sens inverse, un verbe nu et
imprécis se **précise**, il ne se dépouille pas davantage.

**Une idée cohérente par unité.** Un paragraphe d'allégation, un article de contrat, un paragraphe
de lettre porte une idée et les qualificatifs qui s'y rattachent directement. Ce n'est pas « un
verbe par paragraphe ». L'unité se scinde quand elle franchit une frontière de catégorie — la
faute, le préjudice, le lien de causalité; l'obligation, sa modalité, sa sanction. Elle ne se
scinde pas pour séparer un fait de son descripteur.

**Verbes.** Présent pour les faits actuels, passé composé pour les actes accomplis. Le verbe précis
plutôt que le générique : « a constaté » plutôt que « a vu »; « a fait défaut de donner suite »
plutôt que « n'a pas répondu ».

**Ne pas remplir.** Répéter un point sous trois formes ne le renforce pas; une procédure courte est
plus difficile à attaquer.

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
`analyse-documentaire`. Elle produit en revanche la note d'analyse, la théorie de la cause et le
plan d'argumentation — ce dernier étant le document où les citations réapparaissent au grand jour,
devant le tribunal.

Elle ne met pas en forme : en-têtes, cartouches et blocs de signature appartiennent aux gabarits.

## Contrôle avant remise

1. **Famille** — le fichier de la famille a été lu, et le texte suit sa structure.
2. **Faits** — chaque fait allégué est établi ou rapporté, sa source est identifiable, aucun
   crochet n'a été comblé par un fait plausible, et les désignations viennent du dossier.
3. **Mise en forme** — le bloc est exempt d'en-tête, d'intitulé de cour, de bloc de signature, de
   coordonnées et de tout balisage Markdown.
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
9. **Déontologie** — toute obligation professionnelle que l'écrit met en jeu — communication avec
   une partie représentée, engagement pris, franchise envers le tribunal — est signalée; voir
   `deontologie-professionnelle`.

Signaler à l'utilisateur, **hors du bloc**, ce qui reste à décider ou à vérifier : crochets à
combler, montants à confirmer, pièces à coter, dates à valider, désignations à compléter,
propositions de droit non vérifiées. Ce signalement vit à l'extérieur du texte à copier, jamais
dedans.

## Fichiers de référence

Chacun des quatre fichiers de famille s'ouvre sur une section 0 qui dit ce qu'il faut du dossier
avant d'écrire.

- `references/actes-de-procedure.md` — la famille la plus codifiée : unité d'allégation, formule de
  pièce, allégations de caractérisation, dommages, compétence, conclusions, et les variantes.
- `references/actes-juridiques.md` — contrats et actes consensuels : architecture, clauses usuelles,
  et les limites impératives du C.c.Q. qui rendent inopérantes les clauses importées.
- `references/correspondance.md` — mise en demeure et lettres : assises légales de la demeure,
  registre, formules d'appel et de politesse, mentions de réserve.
- `references/notes-internes.md` — note d'analyse, et note de stratégie en deux modes : la théorie
  de la cause et le plan d'argumentation. La famille où les citations sont exigées.
- `references/contamination.md` — tables complètes des marqueurs français et de common law, faux
  amis, lexique de substitution, et la **terminologie anglaise officielle** tirée des versions
  anglaises du C.p.c. et du C.c.Q. À lire pour toute révision d'un texte d'origine incertaine et
  pour toute rédaction en anglais.