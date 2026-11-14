# Pratique civile québécoise

Cinq compétences pour le litige civil et commercial québécois : **établir le droit**, **écrire**,
**qualifier les documents**, **dater**, **se rappeler ce qu'on doit**. Elles se répondent et ne se
recoupent pas.

| Compétence | Répond à | Produit |
|---|---|---|
| `recherche-juridique` | Quelle est la règle? | La fiche, la note de recherche, la vérification de citations |
| `redaction-juridique` | Comment l'écrire? | Le bloc de contenu d'un acte, d'une lettre, d'une note |
| `analyse-documentaire` | Qu'est-ce que ce document, et que vaut-il? | Le registre de tri, la fiche de pièce, le bordereau, la chronologie |
| `calendrier-procedural` | Quand? | Le calendrier daté de l'instance, chaque délai qualifié |
| `deontologie-professionnelle` | Qu'est-ce que je dois, ici? | L'obligation nommée au texte, signalée sans qu'on la demande |

Aucune ne dépend d'un gestionnaire de dossiers. Le plugin `pallas-athena` fournit celui du
cabinet; un autre connecteur, ou aucun, laisse les cinq compétences opérantes. Les connecteurs
publics (sources de droit et calcul déterministe), eux, sont déclarés ici : voir `.mcp.json`,
`mcp_config.json` et `gemini-extension.json`.

---

## Le partage des rôles

`recherche-juridique` **établit ce qui peut être affirmé**. Aucune proposition de droit n'est
avancée ailleurs sans être passée par elle ou par une source que l'utilisateur fournit.

`redaction-juridique` **consomme ce travail et le convertit en texte**. Elle ne construit pas le
fondement; elle le présuppose et signale quand il manque.

`analyse-documentaire` **dit ce qu'un document est, qui peut le voir et ce qu'il prouve**. Elle
alimente les autres — une pièce qualifiée devient une allégation soutenue, un jugement authentifié
devient une autorité, une chronologie fournit ses ancrages au calendrier.

`calendrier-procedural` **dit le jour**. Depuis une date d'ancrage, il déroule la chaîne des délais
du Code de procédure civile, compte selon l'art. 83 et qualifie selon l'art. 84. Il ne touche pas à
la prescription, qui est du droit substantiel et reste à la recherche.

`deontologie-professionnelle` **rappelle l'obligation, au texte, sans qu'on la demande**. Elle est
le second regard du praticien seul : chaque autre compétence porte, en fin de contrôle, une ligne
qui lui renvoie ce qu'elle a aperçu. Elle rappelle; elle n'atteste rien, ne lit l'état d'aucune
vérification et ne dépend d'aucun système de suivi — elle est la seule des cinq à ne porter aucun
besoin du contrat d'information.

Trois disciplines circulent d'une compétence à l'autre et portent le même nom partout :

- le **statut de lecture** d'une autorité (`recherche-juridique`) — citée, résumée, rapportée, lue;
- le **statut du fait** (`redaction-juridique`) — établi, rapporté, administratif, absent;
- le **régime de protection** d'un document (`analyse-documentaire`) — niveaux 0 à 3.

Une autorité, un fait ou un document transmis d'une compétence à l'autre voyage **avec son
statut**, jamais nu.

---

## Le contrat d'information

Les compétences disent **quels renseignements il leur faut**; elles ne disent jamais **par quel
appel les obtenir**. C'est la règle qui les garde indépendantes du logiciel.

Chaque compétence porte une section « Ce qu'il faut du dossier » rédigée dans un vocabulaire
commun de douze besoins :

| Besoin | Ce qu'il recouvre |
|---|---|
| **FICHE** | Qualification du recours, forum, rôle du client, délai inscrit et sa nature |
| **PARTIES** | Désignations exactes, forme juridique, qualité, coordonnées |
| **THÉORIE** | La théorie de la cause telle que l'avocat l'a arrêtée |
| **NOTES** | Ce qui a déjà été écrit au dossier sur la question |
| **INVENTAIRE** | Quels documents le dossier contient, sous quelle catégorie |
| **TEXTE** | Le texte d'un document donné |
| **ÉCHÉANCES** | Protocole, audiences, tâches, portrait de prescription |
| **CORRESPONDANCE** | Les échanges — courriels, lettres, pièces jointes |
| **CALCUL** | Le calcul d'un délai de procédure ou d'intérêts légaux — servi par le connecteur « pratique-civile-outils » (`calendrier_*`, `interets_compute_1619`), à défaut par `scripts/calcul_delai.py` pour les délais, autant que par un gestionnaire de dossiers |
| **GREFFE** | La décomposition d'un numéro de dossier de cour — servi par le connecteur « Jurisprudence » (`greffe_*`, `palais_*`) autant que par un gestionnaire de dossiers |
| **VOCABULAIRE** | Les codes qu'un système accepte en écriture |
| **INSCRIPTION** | Verser un résultat au dossier |

Une compétence d'outillage — `pallas-athena` pour ce cabinet — traduit ces besoins en appels
concrets et porte à elle seule les pièges du connecteur : plafonds, pagination, écritures
irréversibles, vocabulaires fermés. Elle porte aussi les mises en garde sur les champs : rien de ce
qu'un gestionnaire de dossiers rend n'est un fait prouvé.

**L'appui factuel se cherche dans un ordre de préférence**, le même partout : le gestionnaire de
dossiers s'il y en a un de connecté; à défaut, l'avocat, interrogé sur les éléments précis qui
manquent; à défaut encore, la réponse en droit, hypothèses énoncées et crochets apparents. La
compétence dit toujours lequel des trois a servi, et ne bascule jamais en silence sur la mémoire
pour combler.

**Le besoin CORRESPONDANCE n'a pas d'outillage** : il se sert en demandant, et cela se dit.

## Les connecteurs

Ce plugin déclare les connecteurs publics de **sources de droit** et de **calcul déterministe** dont la méthode dépend :

- **`.mcp.json` (Claude)** déclare « Legislation » et « Jurisprudence » par leur nom d'entrée au
  répertoire (`{}`) pour `claude.ai`, où l'autorisation reste attachée au compte sans variable
  d'environnement locale (évitant le déclenchement d'une découverte OAuth sur `401`), ainsi que le
  connecteur public et sans état « `pratique-civile-outils` » (`https://outils.poirierlavoie.ca/mcp`).
- **`mcp_config.json` (Google Antigravity)** et **`gemini-extension.json` (Gemini CLI)** câblent :
  - le point d'entrée Streamable HTTP de « Jurisprudence »
    (`https://jurisprudence.poirierlavoie.ca/mcp` — page publique
    <https://jurisprudence.poirierlavoie.ca/>, dépôt source
    <https://github.com/jpoirierlavoie/MCP-Jurisprudence-Quebec>) avec authentification par en-tête
    `Authorization: Bearer ${MCP_JURISPRUDENCE_SECRET}` (aucun secret n'est déposé ici);
  - le point d'entrée public et sans état « `pratique-civile-outils` »
    (`https://outils.poirierlavoie.ca/mcp`, sans secret requis), qui expose trois outils déterministes
    sans journalisation des charges utiles ni persistance : `calendrier_list_holidays`,
    `calendrier_compute_deadlines` et `interets_compute_1619`.

Aucun **gestionnaire de dossiers** n'y est déclaré, ni nommé nulle part dans les compétences. C'est
la seule frontière, et c'est elle qui rend ce plugin installable chez quelqu'un d'autre.

---

## Le gabarit d'une compétence

Toute compétence de ce plugin respecte un **contrat structurel à sept invariants**, dans cet ordre. Une compétence nouvelle qui s'en écarte est à corriger, non à tolérer; entre la méthode et le périmètre, une compétence peut insérer des sections intermédiaires propres à ses garde-fous ou à ses modes.

1. **Ce que fait la compétence** — ouverture sous le titre `# `, en deux ou trois phrases, et sa place dans la famille.
2. **Le principe directeur** — premier intertitre `## ` (`## Le principe qui gouverne` ou `## La règle asymétrique`), la règle structurante dont tout le reste découle.
3. **La méthode** — `## La méthode`, étapes ordonnées sous des titres qui nomment l'opération (suivie, au besoin, des intertitres `## ` propres aux modes ou aux garde-fous de la compétence).
4. **Ce qu'il faut du dossier** — `## Ce qu'il faut du dossier`, exprimé dans les douze besoins du tableau ci-dessus, jamais en noms d'outils de gestionnaire.
5. **Le périmètre** — `## Le périmètre`, ce que la compétence ne fait pas et à qui cela revient (premier volet du triptyque final immuable).
6. **Contrôle avant remise** — `## Contrôle avant remise`, la liste de vérification numérotée.
7. **Fichiers de référence (et outillage local)** — `## Fichiers de référence`, ou `## Fichiers de référence et outillage local` lorsque la compétence embarque un utilitaire Python autonome sous `scripts/`, un par ligne avec le moment où l'ouvrir ou l'exécuter.

## Les conventions d'écriture

- **Un titre nomme une opération**, pas un effet d'annonce. « La règle asymétrique » plutôt que
  « La règle asymétrique — la plus importante de toutes ».
- **L'infinitif ou l'impératif**, jamais le tutoiement, jamais la deuxième personne du pluriel.
  Ce sont des consignes, pas un discours à l'utilisateur.
- **Une règle, sa raison, en une phrase chacune.** La raison reste : c'est elle qui empêche de
  contourner la règle dans un cas non prévu.
- **Un renvoi croisé nomme la compétence par son identifiant**, entre accents graves. Il a sa place
  en section 1 (le partage des rôles), en section 5 (le périmètre), et partout où une règle confie
  effectivement une décision à une autre compétence. Nulle part ailleurs : un renvoi décoratif
  périme.
- **Aucun nom de gestionnaire de dossiers ni de ses outils** dans ce plugin — c'est la seule
  frontière, et elle est étanche. Les **connecteurs de sources de droit et de calcul** sont au contraire nommés
  librement : ce plugin déclare « Legislation », « Jurisprudence » et « pratique-civile-outils » dans
  ses manifestes MCP (`.mcp.json`, `mcp_config.json`, `gemini-extension.json`), et ses fichiers
  appellent leurs outils par leur nom, parce que la méthode n'a de sens qu'appliquée à des appels
  précis. Le contrôle se fait par `verifier.py`, qui ne doit rien retourner.
- **Les chiffres sont des hypothèses** — seuils, délais, montants. Ils dérivent avec les
  modifications législatives et se revérifient aux sources avant emploi.
- **Progressive disclosure** : le SKILL.md reste sous 3 000 mots; le détail va dans
  `references/`, chaque fichier annoncé avec le moment où il faut l'ouvrir, et tout calcul ou
  inspection locale déterministe va dans `scripts/` en bibliothèque standard Python uniquement.

## Ajouter une compétence

1. La faire entrer dans le partage des rôles — si elle empiète, c'est qu'elle appartient à une
   compétence existante.
2. Respecter les sept invariants et le triptyque final immuable (`Le périmètre` → `Contrôle avant
   remise` → `Fichiers de référence`).
3. N'exprimer ses besoins d'information qu'en termes du tableau ci-dessus; si un besoin nouveau
   apparaît, l'ajouter ici d'abord, puis dans l'outillage.
4. Rédiger la description du frontmatter avec ses amorces en français **et** en anglais, et la
   phrase « Ne pas utiliser pour… » qui la sépare de ses voisines.
5. Passer le contrôle : exécuter `python verifier.py` (aucun nom d'outil interdit, tout fichier
   annoncé existe, tout renvoi pointe une compétence réelle) et ajouter un scénario dans
   `evals/scenarios.json`.

---

## Installation et compatibilité

Ce dépôt sert sans duplication des compétences (`skills/`) **Claude**, **Google Antigravity**
et **Gemini CLI** : chaque plateforme lit son propre manifeste et ignore les autres.

- **Claude (`claude.ai` et `Claude Code`)** — `.claude-plugin/plugin.json`,
  `.claude-plugin/marketplace.json` et `.mcp.json` :
  - dans `claude.ai`, synchroniser le dépôt depuis *Paramètres de l'organisation → Plugins et
    compétences*;
  - dans `Claude Code`, ajouter le catalogue puis installer le greffon :
    `/plugin marketplace add jpoirierlavoie/pratique-civile-quebecoise` puis
    `/plugin install pratique-civile-quebecoise@pratique-civile-quebecoise`; s'il n'est pas hérité
    du compte `claude.ai`, enregistrer le connecteur Streamable HTTP `Jurisprudence` avec :
    `claude mcp add --transport http Jurisprudence https://jurisprudence.poirierlavoie.ca/mcp --header "Authorization: Bearer ${MCP_JURISPRUDENCE_SECRET}"`.
  - `.mcp.json` déclare également « `pratique-civile-outils` » (`https://outils.poirierlavoie.ca/mcp`),
    sans secret requis.
- **Google Antigravity** — `plugin.json`, `mcp_config.json` et `assets/logo.svg` :
  - installer via `agy plugin install https://github.com/jpoirierlavoie/pratique-civile-quebecoise.git`,
    ou copier le contenu dans `~/.gemini/config/plugins/pratique-civile-quebecoise`;
  - `mcp_config.json` câble directement `jurisprudence`
    (`https://jurisprudence.poirierlavoie.ca/mcp`) et `pratique-civile-outils`
    (`https://outils.poirierlavoie.ca/mcp`, sans secret) : renseigner `MCP_JURISPRUDENCE_SECRET` sur la
    page du plugin puis l'activer, et déclarer `Legislation` dans
    `~/.gemini/config/mcp_config.json` tant que son point d'entrée n'est pas câblé ici.
- **Gemini CLI** — `gemini-extension.json` :
  - installer via `gemini extensions install https://github.com/jpoirierlavoie/pratique-civile-quebecoise`
    — `gemini-extension.json` préconfigure `jurisprudence`
    (`https://jurisprudence.poirierlavoie.ca/mcp`), demande de manière sécurisée (`sensitive: true`)
    le secret `MCP_JURISPRUDENCE_SECRET`, et câble `pratique-civile-outils`
    (`https://outils.poirierlavoie.ca/mcp`) sans secret requis.
- **Contrôle** — exécuter `python verifier.py` depuis la racine du dépôt; le script valide les
  manifestes, les en-têtes YAML, les sept invariants structurels, les renvois aux fichiers de
  référence et l'étanchéité du contrat d'information, et ne retourne rien lorsque tout est conforme.
  Exécuter ensuite `python evals/executer_evals.py --auto-test` pour vérifier les scripts locaux et
  les scénarios de régression dans `evals/`.
