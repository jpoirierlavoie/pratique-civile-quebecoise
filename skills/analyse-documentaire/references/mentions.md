# Mentions attendues

À lire au temps 2 de la méthode, **après** avoir arrêté la nature. C'est la nature qui commande les
mentions à chercher, jamais l'inverse.

*Ancrages vérifiés au texte officiel consolidé au 2026-04-07.*

## Les trois statuts d'une mention

| Statut | Ce que l'absence signifie |
|---|---|
| **Exigée** — le texte la commande | Une **irrégularité**, à signaler. Pas une erreur d'analyse : un acte de procédure sans district judiciaire est un acte incomplet |
| **Usuelle** — l'usage la porte constamment, aucun texte ne l'exige | Rien. Ne pas la signaler, ne pas la peser |
| **Sans objet** — la nature ne la comporte pas | Rien. Le champ est **nul**, il n'est pas vide |

**Ne jamais combler un champ par déduction.** Un numéro de dossier de cour trouvé dans le nom du
fichier, un district inféré du nom du tribunal, une date reconstituée à partir d'un horodatage de
téléversement : ce sont des inventions, et elles se propagent en silence. Le champ reste vide, et
l'absence se rapporte.

## Les trois cas où une absence est normale, et ne pèse pas

1. **La mention est sans objet pour la nature.** Un contrat, un courriel, une photographie n'ont ni
   tribunal, ni district judiciaire, ni numéro de dossier de cour.
2. **Le document est un projet non déposé.** Pas de numéro de dossier de cour, pas de timbre de
   greffe, pas de preuve de notification : c'est cohérent avec un projet, et cela **oriente la
   qualification** au temps 3 plutôt que de la contredire.
3. **Le document est un extrait ou une page isolée d'un ensemble.** L'en-tête, la signature ou la
   cote vivent sur une autre page. Le dire, et demander l'ensemble plutôt que de conclure.

Hors ces trois cas, l'absence d'une mention **exigée** est un signalement.

**Ces trois statuts calibrent la confiance dans la qualification.** L'absence d'une mention exigée
pèse; l'absence d'une mention seulement usuelle ne pèse pas; et les trois cas ci-dessus ne pèsent
pas du tout. Une qualification dont toutes les mentions exigées sont présentes se donne pour haute;
une qualification à laquelle il manque une mention exigée se donne pour moyenne; une qualification
appuyée sur un fragment ou sur des métadonnées seules se donne pour faible.

---

## Acte de procédure

L'art. 99 C.p.c. énonce la totalité des mentions exigées. Les voici, telles que le texte les pose.

| Mention | Statut | Source |
|---|---|---|
| Nature de l'acte | Exigée | art. 99 al. 1 |
| Objet | Exigée | art. 99 al. 1 |
| Faits qui le justifient | Exigée | art. 99 al. 1 |
| Conclusions recherchées | Exigée | art. 99 al. 1 |
| Énoncés numérotés consécutivement, clairs, précis, concis, dans un ordre logique | Exigée | art. 99 al. 1 |
| Tribunal saisi | Exigée | art. 99 al. 2 |
| District judiciaire | Exigée | art. 99 al. 2 |
| Numéro du dossier | Exigée | art. 99 al. 2 |
| Nom des parties | Exigée | art. 99 al. 2 |
| Date à laquelle l'acte est fait | Exigée | art. 99 al. 2 |
| Identification de l'auteur — signature ou ce qui en tient lieu | Exigée | art. 99 al. 3 |
| Cartouche (CANADA / PROVINCE DE QUÉBEC / DISTRICT DE …) | Usuelle | — |
| Coordonnées de l'avocat et du cabinet | Usuelle | — |
| Indication des pièces au soutien | **Exigée** — dans l'avis d'assignation pour la demande; dans l'acte lui-même ou un avis qui y est joint pour tout autre acte | art. 145 al. 1, 247 C.p.c. |
| Bordereau ou liste de pièces en pièce jointe | Usuelle — c'est la forme, non l'indication | — |

**Le numéro de dossier est le discriminant du temps 3.** Son absence n'est une irrégularité que si
l'acte a été déposé; sur un projet, elle est normale et signale précisément qu'il s'agit d'un
projet. C'est le greffier qui attribue ce numéro, au dépôt de la demande introductive (art. 107 al.
1 C.p.c.).

**Variantes propres à certaines sous-natures :**

| Sous-nature | Mention supplémentaire | Source |
|---|---|---|
| `PROC_AVIS_ASSIGN` | Indication des pièces au soutien de la demande; délai de 15 jours pour répondre | art. 145 |
| `PROC_DEM_INSTANCE` écrite | Date, heure et lieu de présentation | art. 101 al. 1 |
| `PROC_DEM_INSTANCE` reposant sur des faits hors dossier | Serment de celui qui les allègue | art. 101 al. 3 |
| `PROC_DECL_SERMENT` | Jour et lieu du serment; nom et adresse de celui qui le prête; nom et qualité de celui qui le reçoit | art. 105 al. 2 |
| `PROC_PROTOCOLE` | Les neuf points de l'art. 148 al. 2, plus les conventions, les questions en litige, la considération portée aux modes privés de PRD, le temps et les coûts prévisibles, et les échéances | art. 148 |
| `PROC_DECL_APPEL` | Contenu de la déclaration (art. 353); signification à l'intimé et notification à l'avocat de première instance avant l'expiration du délai d'appel (art. 358 al. 1) | art. 352, 353, 358 |

## Jugement

| Mention | Statut |
|---|---|
| Tribunal, district, numéro de dossier de cour | Exigée en pratique — un jugement sans elles est un extrait ou un projet |
| Nom des parties | Exigée |
| Date | Exigée |
| Dispositif | Exigée — c'est ce qui en fait un jugement |
| Nom et signature du juge | Exigée |
| Motifs | Usuelle en première instance |
| Citation neutre | Usuelle — présente sur les décisions diffusées, absente sur plusieurs originaux du greffe |

**`JUG_ARRET` :** l'art. 389 C.p.c. exige, outre le dispositif, le nom des juges qui ont entendu
l'appel, avec mention de celui ou de ceux qui ne partagent pas l'opinion de la majorité; l'arrêt est
motivé, à moins qu'il ne renvoie à des opinions exprimées par les juges.

**Un dispositif sans motifs n'est pas une irrégularité.** Un dispositif absent, en revanche, veut
dire que le document n'est pas un jugement : c'est un projet, un extrait ou des motifs seuls.

## Procès-verbal de signification

L'art. 119 al. 2 C.p.c. énumère six mentions, toutes exigées.

| Mention | Source |
|---|---|
| Numéro du dossier du tribunal et nom des parties | art. 119 al. 2 (1°) |
| Nature du document signifié | art. 119 al. 2 (2°) |
| Lieu, date et **heure** de la signification | art. 119 al. 2 (3°) |
| Nom de la personne à qui le document a été remis et, s'il y a lieu, sa qualité — ou le lieu où il a été laissé | art. 119 al. 2 (4°) |
| Refus de recevoir signification ou échec de la tentative, le cas échéant | art. 119 al. 2 (5°) |
| État des honoraires et des frais | art. 119 al. 2 (6°) |
| Serment professionnel de l'huissier | art. 119 al. 1 |

**`PV_SIGNIFICATION_DESIGNEE` :** la personne désignée indique son nom, sa qualité et son adresse,
et le procès-verbal est appuyé d'un récépissé — à moins que le destinataire ait refusé de le donner,
auquel cas le refus est consigné (art. 120 al. 1 C.p.c.).

**Ce document est celui dont les mentions comptent le plus** : la date et l'heure font courir des
délais, et le nom de la personne signifiée détermine par rapport à qui. Une signification incomplète
se signale immédiatement. Une date de signification relevée ici se **rapporte**, elle ne se convertit
jamais en échéance calculée.

## Correspondance

| Mention | Statut |
|---|---|
| Expéditeur et destinataire réels — copies conformes comprises | Exigée pour qualifier : sans eux, ni sous-nature ni régime ne se déterminent |
| Date | Exigée pour qualifier |
| Objet | Usuelle |
| Mention de transmission (courriel, télécopie, poste recommandée) | Usuelle — mais c'est elle qui établit le mode |
| Mention de réserve (« sous toutes réserves », « privilégié ») | Usuelle — son absence n'écarte pas le régime, sa présence ne le crée pas à elle seule |
| Signature ou bloc d'expéditeur | Usuelle |

**`CORR_MISE_DEMEURE` :** ce qui la caractérise est la **sommation** — l'objet de l'obligation, le
défaut reproché, ce qui est exigé, le délai d'exécution accordé, et la sanction annoncée du défaut
(art. 1595 C.c.Q. pour le principe de la demande extrajudiciaire). Une lettre qui discute sans
sommer n'est pas une mise en demeure, quel que soit son titre. Relever la date **et** le mode de
transmission : ils commandent le point de départ.

## Pièce et preuve

| Mention | Statut |
|---|---|
| Cote de pièce (P-1, D-3, PC-2) | Exigée pour retenir `PIECE_COMMUNIQUEE`; sans objet autrement |
| Date propre du document | Exigée pour qualifier — à distinguer de la date de téléversement, qui n'est pas la sienne |
| Auteur ou émetteur | Exigée pour qualifier |
| Signature des parties | Exigée pour un acte sous seing privé (art. 2826 C.c.Q.); **sans objet** pour un écrit d'entreprise (art. 2831) |
| Destinataire | Exigée pour un courriel |
| Totaux, période, devise | Exigée pour un relevé ou une facture |
| Métadonnées d'origine (appareil, horodatage, géolocalisation) | Usuelle pour une photographie — souvent absentes après une capture d'écran ou un envoi par messagerie |

**`PREUVE_RAPPORT_EXPERT` :** identité et qualifications de l'expert, mandat reçu, méthode,
documents consultés, conclusions, date et signature. Le rapport tient lieu du témoignage de
l'expert, mais seulement s'il a été communiqué et versé au dossier dans les délais (art. 293
C.p.c.) — relever s'il porte une marque de communication, et le signaler quand il n'en porte pas.

**Une pièce n'a ni tribunal, ni district, ni numéro de dossier de cour**, sauf lorsqu'elle est
elle-même un acte de procédure ou un jugement produit comme pièce. Ces champs sont **sans objet**.

## Documents du cabinet

| Sous-nature | Mentions attendues |
|---|---|
| `CAB_MANDAT` | Identité du client, objet du mandat, base d'honoraires, taux ou pourcentage, déboursés, date, signatures |
| `CAB_FACTURE` | Numéro, date, période, dossier, honoraires, déboursés, taxes, total, solde |
| `CAB_DEBOURSE` | Fournisseur, date, objet, montant, rattachement au dossier |
| `CAB_MEMO` | Auteur, date, objet. Rien d'autre n'est exigé — c'est un document interne |

## Ce qui se rapporte, et comment

Pour chaque document, une ligne suffit en mode tri. En mode pièce, la rubrique 1 reprend les
mentions relevées et **nomme celles qui manquent**, avec leur statut :

> Demande introductive — tribunal et district présents, parties nommées, date du 4 mars.
> **Numéro de dossier de cour absent** : cohérent avec un projet non déposé (cas normal 2).
> Signature absente : à vérifier sur la dernière page, qui n'est pas au document fourni.
