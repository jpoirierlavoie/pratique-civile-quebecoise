---
name: calendrier-procedural
description: >-
  Construire et vérifier le calendrier d'une instance civile québécoise (régime ordinaire,
  Cour du Québec art. 535.1 s., appel) : depuis une date d'ancrage — signification, avis
  d'assignation, notification, jugement, acceptation du protocole —, dérouler la chaîne des
  délais du C.p.c., compter selon l'art. 83, qualifier le délai et dire ce que son dépassement
  emporte. Utiliser dès qu'une date de procédure est en jeu, lorsqu'une pièce datée est relevée
  par analyse-documentaire, ou avant de rédiger avec redaction-juridique. Amorces — quel est le
  délai, jusqu'à quand, est-ce échu, combien de jours reste-t-il, calcule l'échéance, délai de
  rigueur. En anglais — deadline, time limit, when is it due, strict time limit, days left. Ne pas
  utiliser pour la prescription, qui relève de recherche-juridique, ni pour inscrire une échéance.
---

# Calendrier procédural

Répond à la question que les trois autres compétences ne posent pas : **quand?** Depuis une date
d'ancrage, elle déroule la chaîne des délais de l'instance, compte chacun selon l'art. 83 C.p.c.,
le qualifie, et dit ce que son dépassement emporte. `recherche-juridique` établit pourquoi un délai
existe et ce qu'il vaut en droit; `redaction-juridique` écrit l'acte qu'il commande; cette
compétence-ci dit le jour.

## Le principe qui gouverne

**Un délai se qualifie avant de se compter, et se compte depuis le texte, jamais depuis la
mémoire.** La qualification vient d'abord parce que la conséquence du dépassement en dépend : un
délai que le Code qualifie de rigueur ne se prolonge que si le tribunal est convaincu que la partie
a été en fait dans l'impossibilité d'agir plus tôt; tout autre délai peut être prolongé ou, en cas
d'urgence, abrégé (art. 84 C.p.c.). Une échéance calculée juste mais qualifiée faux mène à un
mauvais conseil.

Un délai ne s'écrit jamais dans le calendrier sans son article. Un délai récité est indistinguable
d'un délai inventé, et les délais sont ce que la loi modifie le plus souvent.

## La méthode

**1. Fixer l'ancrage, et sa nature.** La chaîne ne part pas de « la date du jugement » mais de
l'un des événements que le Code nomme : la signification, la notification, l'avis du jugement, le
jugement rendu à l'audience, l'acceptation présumée ou l'établissement du protocole, la disparition
d'une cause d'empêchement. Deux ancrages voisins donnent deux calendriers différents — un jugement
rendu à l'audience fait courir l'appel du jour même; un jugement notifié le fait courir de l'avis.
Trois ancrages trompent : la notification par moyen technologique faite après 17 h, un samedi ou
un jour férié est réputée faite à 8 h le jour ouvrable suivant (art. 111 al. 2); le jugement
rectifié sur son dispositif fait courir l'appel depuis la rectification (art. 338 al. 3); le
jugement rendu sur une demande issue d'une scission n'est appelable qu'à compter de l'avis du
jugement qui met fin à l'instance (art. 211 al. 2). Si l'ancrage n'est pas établi par une pièce,
le dire et le marquer.

**2. Identifier le régime.** Le forum et la matière commandent des chaînes différentes :

- **Instance ordinaire en Cour supérieure (ou matière dépassant le seuil de l'art. 535.1).** Le
  protocole se dépose dans les 45 jours, ou dans les trois mois en matière familiale; la mise en
  état se fait dans les six mois, ou dans un an en matière familiale.
- **Régime simplifié devant la Cour du Québec (art. 535.1 à 535.15 C.p.c.).** S'applique de plein
  droit à toute demande visée par l'art. 35 dont la valeur est inférieure à 100 000 $ hors
  intérêts : aucun protocole de l'instance (535.2), ancrage sur la **signification de l'avis
  d'assignation** avec la séquence 20 / 45 / 95 / 110 / 130 à 160 jours et inscription au plus
  tard dans les 6 mois (535.4 à 535.13). Dans la tranche concurrente (75 000 $ à moins de
  100 000 $), le choix du demandeur déposé au greffe tranche le régime : Cour du Québec = régime
  simplifié; Cour supérieure = protocole ordinaire.

Les règlements de pratique du tribunal et du district s'ajoutent au Code : les lire à la source
pour l'instance en cause, ils ne sont pas reproduits ici.

**3. Dérouler la chaîne.** Prendre la table de `references/chaine-de-l-instance.md` et n'en
retenir que les maillons que l'ancrage déclenche. Une chaîne complète pour une question ponctuelle
noie l'échéance qui compte.

**4. Compter selon l'art. 83.** Le délai court à compter de l'acte, de l'événement, de la décision
ou de la notification qui en est la source. En jours, le jour du point de départ ne compte pas,
celui de l'échéance compte. En mois, le délai expire le jour du dernier mois qui porte le même
quantième; à défaut, le dernier jour du mois. Il expire à 24 h; s'il tombe un samedi ou un jour
férié, il est prolongé au premier jour ouvrable qui suit. Les jours fériés, et les règles d'heures
qui déplacent une notification ou un dépôt au jour ouvrable suivant (art. 107 al. 4, 111 al. 2),
sont dans `references/jours-non-juridiques.md`. Quand le besoin **CALCUL** est servi par un outil
connecté (`calendrier_compute_deadlines`, et `calendrier_list_holidays` pour lister les jours non
juridiques), s'en servir et rapporter son résultat; sinon, lorsque l'exécution Python locale est
disponible, exécuter `scripts/calcul_delai.py` (`python scripts/calcul_delai.py <AAAA-MM-JJ> --jours <N>`)
plutôt que de compter mentalement, et dans tous les cas montrer le compte visible étape par étape
(ancrage, déplacement éventuel selon l'art. 111 al. 2, jour 1, date brute, report selon l'art. 83,
date effective).

**5. Qualifier chaque délai.** Quatre statuts : **de rigueur** quand le Code le dit — art. 173,
art. 347 al. 3, art. 363 al. 1; **ordinaire** pour tout autre délai du Code, y compris ceux dont
la sanction est lourde — la péremption de l'art. 107 al. 3, la caducité de l'appel de l'art. 376,
dont la prolongation doit être demandée avant l'expiration (art. 373 al. 3); **conventionnel**
quand il vient du protocole ou d'une entente; **judiciaire** quand le tribunal l'a fixé —
ordinaire en principe, de rigueur seulement quand le Code le dit du délai fixé, comme le délai de
mise en état prolongé en conférence de gestion (art. 173 al. 2), et prolongeable pour seul motif
impérieux quand il a été fixé après levée de la présomption de désistement (art. 177 al. 2). Dire
pour chacun ce que le dépassement emporte — déchéance, présomption de désistement, péremption,
caducité, forclusion, irrecevabilité, autorisation requise — avec l'article qui le dit.

**6. Rendre le tableau.** Une ligne par échéance : date, ce qui doit être fait, ancrage, article,
statut, conséquence du dépassement. Les échéances passées y figurent, marquées; celles qui
dépendent d'une date inconnue portent un crochet, pas une estimation.

**7. Signaler ce qui n'est pas dans le calendrier.** La prescription du droit d'action n'y est pas
— elle relève du droit substantiel et de `recherche-juridique`, et une instance introduite à temps
peut porter un recours prescrit. Les délais de l'énoncé commun et des mémoires d'appel sont dans
le Code (art. 372 al. 2, 373; sanction à l'art. 376) et dans la chaîne; ce que le Règlement de la
Cour d'appel du Québec en matière civile y ajoute — forme des actes, délais fixés par la gestion de l'appel — se lit à la source,
comme les règlements de pratique de première instance. Le dire en fin de tableau.

## Ce que l'art. 82 dit, et ne dit pas

Les tribunaux ne siègent pas les samedis ni les jours fériés, ni les 26 décembre et 2 janvier, qui
sont considérés jours fériés en matière de procédure civile. Ces jours reportent une échéance.

Les tribunaux de première instance **ne sont pas tenus de siéger** du 30 juin au 1er septembre ni
du 20 décembre au 7 janvier. **Ce ne sont pas des suspensions de délais.** Un délai de 30 jours qui
court en juillet court en juillet; il n'est prolongé que s'il expire un samedi ou un jour férié.
L'erreur inverse — compter la période estivale comme suspendue — est fréquente et coûte un droit
d'appel. La règle se dit en toutes lettres dans le tableau quand une échéance tombe dans l'une de
ces périodes.

## Ce qu'il faut du dossier

Pour l'ancrage : la date exacte et sa nature — signification ou notification, à qui, par quel mode
—, établie par la pièce qui la porte : procès-verbal de signification, preuve de notification,
avis de jugement. Les obtenir dans l'ordre de préférence commun au plugin : le gestionnaire de
dossiers s'il y en a un de connecté — besoins **ÉCHÉANCES** pour ce qui est déjà inscrit,
**FICHE** pour le forum et la matière, **INVENTAIRE** et **TEXTE** pour la pièce qui date
l'ancrage —; à défaut, l'avocat, interrogé sur la date précise et sa preuve; à défaut encore, le
calendrier se construit sur une date hypothétique, marquée comme telle à chaque ligne.

Le besoin **CALCUL** sert le compte (`calendrier_compute_deadlines` ou outil du gestionnaire, à défaut `scripts/calcul_delai.py` en local). Le besoin **INSCRIPTION** sert à
proposer chaque échéance à l'agenda : **une échéance qui n'existe que dans le tableau n'existe
nulle part.** Proposer l'inscription, ne pas l'exécuter sans instruction.

Comment servir ces besoins dépend du système — c'est l'affaire d'une compétence d'outillage, s'il
en existe une.

## Le périmètre

Cette compétence **ne calcule pas la prescription**. Le point de départ d'un délai de prescription
est une question de fait et de droit substantiel; il relève de `recherche-juridique` (lire
`../recherche-juridique/SKILL.md`), avec la grille des préalables. Une échéance de prescription
qu'on lui demanderait se renvoie là-bas.

Elle **ne lit pas les règlements de pratique à la place de l'avocat** : elle dit qu'ils s'ajoutent
au Code et lesquels s'appliquent au forum, et elle les lit à la source quand la question en dépend.

Elle **n'inscrit rien** : elle propose, ligne par ligne, et l'avocat décide. Elle ne rédige pas
l'acte que l'échéance commande — enchaîner avec `redaction-juridique` (lire
`../redaction-juridique/SKILL.md`) si l'utilisateur demande l'acte correspondant.

Elle ne verse jamais le contenu d'une pièce dans une requête de recherche web.

## Contrôle avant remise

1. **Ancrage** — la date de départ est nommée par sa nature et par la pièce qui l'établit, ou
   marquée hypothétique.
2. **Régime** — forum, matière et règlement de pratique applicable sont identifiés.
3. **Articles** — chaque ligne porte l'article qui fonde le délai, lu à la source dans cette
   conversation.
4. **Compte** — le jour de départ n'est pas compté, celui de l'échéance l'est; les mois expirent au
   quantième; les samedis, fériés, 26 décembre et 2 janvier ont reporté ce qu'ils devaient; une
   notification technologique tardive ou un dépôt hors heures a été replacé au jour ouvrable
   suivant.
5. **Qualification** — chaque délai porte son statut, et la conséquence de son dépassement; aucun
   délai n'est dit de rigueur que le Code ne qualifie ainsi.
6. **Périodes de non-siège** — aucune n'a été traitée comme une suspension.
7. **Hors calendrier** — la prescription, les règlements de pratique et le Règlement de la Cour
   d'appel sont renvoyés là où ils vivent, en toutes lettres.
8. **Déontologie** — toute obligation professionnelle aperçue concrètement en dressant le
   calendrier (p. ex. délai échu par erreur de l'avocat, art. 48 du Code de déontologie) est
   signalée avec lecture de `../deontologie-professionnelle/SKILL.md`; sans déclencheur concret,
   aucune mention générique.

## Fichiers de référence et outillage local

- `scripts/calcul_delai.py` — utilitaire local autonome en bibliothèque standard Python pour compter
  les délais en jours ou en mois selon les art. 82, 83, 107 al. 4 et 111 al. 2 C.p.c. (`--json`,
  `--a-rebours`, `--technologique`, `--heure`). À exécuter au besoin lors de l'étape 4.
- `references/chaine-de-l-instance.md` — la table des maillons : événement déclencheur, ce qui
  doit être fait, délai, article, statut, conséquence. À lire à chaque calendrier, en n'en retenant
  que les maillons déclenchés.
- `references/jours-non-juridiques.md` — les jours fériés de l'art. 61 de la Loi d'interprétation,
  les ajouts de l'art. 82 C.p.c., les règles d'heures des art. 107 et 111 qui déplacent un dépôt ou
  une notification, et la façon de les appliquer. À lire au moment de compter. Le fichier est
  daté; le revoir chaque année.
