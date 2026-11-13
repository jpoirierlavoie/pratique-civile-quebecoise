# Le bordereau

La liste des pièces d'un acte ou d'un dossier : ce qu'elle contient, ce qu'elle contrôle, ce
qu'elle signale. À lire en mode bordereau.

*Ancrages vérifiés au texte officiel consolidé au 2026-04-07. Les conventions de cotation sont des
usages, non des règles du Code; elles sont marquées comme telles.*

## Ce que le Code exige, et où

| Moment | Ce qui est exigé | Article |
|---|---|---|
| Avis d'assignation | L'**indication des pièces** au soutien de la demande; le demandeur les communique au défendeur dans les plus brefs délais, selon les modalités convenues | 145 al. 1 C.p.c. |
| Tout acte de procédure | Les pièces au soutien sont indiquées **dans l'acte lui-même ou dans un avis qui y est joint** | 247 C.p.c. |
| Défense | Le défendeur communique au demandeur les pièces au soutien de la défense dans les plus brefs délais, selon les modalités convenues | 170 al. 3 C.p.c. |
| Protocole de l'instance | Les modalités et le délai de communication des pièces y sont fixés | 246 al. 1 C.p.c. |
| Déclaration de mise en état | **L'inventaire des pièces et des autres éléments de preuve communiqués** aux autres parties | 174 al. 1 (2°) C.p.c. |
| Instruction | Production au greffe au moins 15 jours avant, ou 3 jours si la date est fixée à moins de 15 jours | 250 C.p.c. |
| Contestation d'une pièce | Formalités, origine ou intégrité contestées : au plus tard avant l'inscription, par déclaration sous serment | 262 C.p.c. |

**Le bordereau est donc trois choses selon le moment** : la liste jointe à l'acte (145, 247),
l'inventaire de ce qui a été communiqué (174), et la liste de ce qui est produit (250). Dire
lequel on dresse, parce que les colonnes qui comptent ne sont pas les mêmes.

## Les colonnes

| Colonne | Contenu | D'où elle vient |
|---|---|---|
| **Cote** | P-1, D-1, PC-1… telle que l'acte la porte | L'acte, jamais une renumérotation |
| **Désignation** | Ce que la pièce est, en une ligne : nature, parties, objet | Temps 1 de la méthode — la nature arrêtée, pas le nom de fichier |
| **Date propre** | La date du document lui-même | Temps 2 — jamais la date de téléversement ni de numérisation |
| **Régime** | Le niveau de protection retenu | Temps 3 — une pièce cotée est présumée publique; une marque de régime protégé sur une pièce cotée est un signalement de renonciation possible |
| **Communiquée** | Oui, date et mode; non; ou inconnu | La preuve de communication, pas la mention dans l'acte : indiquer une pièce n'est pas la communiquer |
| **Produite** | Oui, date; non; sans objet | Le timbre du greffe ou le récépissé |
| **Forme** | Original, copie, copie certifiée, document technologique; **en liasse** le cas échéant | Le document tel qu'il est; « en liasse » se rend par *filed jointly* en anglais |
| **Signalement** | Ce qui cloche : voir ci-dessous | — |

## Les trois signalements du bordereau

**La cotation suit l'ordre de première invocation dans l'acte, en numérotation continue.** C'est
la règle de rédaction — elle vit dans `redaction-juridique`, fichier des actes de procédure —, et
le bordereau la **contrôle** : il lit l'acte, relève chaque première invocation, et compare.

| Signalement | Ce que c'est | Ce qu'on écrit |
|---|---|---|
| **Saut de numéro** | P-1, P-2, P-4 : le P-3 manque, ou a été retiré sans renumérotation | « P-3 absent de l'acte et de la liste » |
| **Invocation sans cote** | L'acte cite un document — « le contrat du 4 mars » — sans le coter | « Contrat du 4 mars invoqué au par. 12, non coté » |
| **Cote sans pièce** | La liste porte une cote que l'acte n'invoque nulle part, ou dont le document n'est pas au dossier | « P-7 listée, invoquée nulle part »; « P-7 listée, document introuvable » |
| **Ordre rompu** | P-5 est invoquée pour la première fois avant P-4 | « P-5 invoquée au par. 8, P-4 au par. 11 : ordre de première invocation inversé » |
| **Doublon** | Le même document sous deux cotes, ou deux documents sous une cote | « P-2 et P-9 : même document » |

Un signalement n'est pas une correction. Le bordereau constate; l'avocat renumérote, ou décide de
ne pas le faire — une renumérotation après communication a un coût, et ce n'est pas au bordereau
de le trancher.

## Ce que le bordereau n'est pas

Il **ne qualifie pas au fond** : la force probante d'une pièce relève du mode pièce, et le
bordereau porte le régime, non la valeur. Il **ne décide pas** ce qui doit être coté : c'est la
rédaction. Il **n'établit pas la communication** : il rapporte la preuve qu'on lui montre, et
« inconnu » est une réponse honnête quand aucune preuve n'est au dossier.

## Gabarit

Une ligne par pièce, dans l'ordre des cotes. En tête, ce qu'on dresse et pour quel acte; en pied,
les signalements et ce qui manque.

    BORDEREAU — Demande introductive d'instance, [intitulé], [date de l'acte]
    Liste des pièces indiquées (art. 247 C.p.c.)

    | Cote | Désignation | Date | Régime | Communiquée | Forme |
    |---|---|---|---|---|---|
    | P-1 | Contrat de vente entre [A] et [B] | 2025-03-04 | Public (cotée) | Oui — 2026-05-12, courriel | Copie |
    | P-2 | Mise en demeure de [A] à [B] | 2025-11-20 | Public (cotée) | Oui — 2026-05-12, courriel | Copie |
    | P-3 | Échange de courriels [A]–[B], 12 au 19 novembre 2025, en liasse | 2025-11-12 à 19 | Public (cotée) | Non | Copies, en liasse |

    Signalements : P-3 non communiquée; la mention « en liasse » couvre six courriels — les dater
    individuellement si l'un est invoqué seul. Aucun saut de numéro; ordre de première invocation
    respecté (par. 6, 9, 14).

En anglais, la colonne « Forme » rend « en liasse » par *filed jointly*, et la terminologie suit la
version anglaise officielle du Code — *exhibit*, *summons*, *originating application* —, jamais une
traduction.
