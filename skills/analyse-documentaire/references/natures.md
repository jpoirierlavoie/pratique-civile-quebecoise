# Natures et sous-natures

Le vocabulaire de classification. À lire au temps 1 de la méthode, avant toute extraction.

**Ce vocabulaire est fermé.** Ne jamais inventer un code. Si aucun ne convient, le dire, proposer
le plus proche, et signaler l'écart. Un code inventé passe le contrôle de forme et casse tout ce
qui s'appuie dessus.

**Si un système refuse un code que cette table porte, la table est périmée.** Le dire et s'arrêter
là, plutôt que d'y substituer un code voisin : une substitution silencieuse produit un classement
faux que personne ne relira.

**La catégorie se dérive de la sous-nature, elle ne se choisit pas.** C'est ce qui rend impossible
d'en fabriquer une. Un système connecté qui accepte la sous-nature dérivera lui-même la catégorie,
le niveau de protection et la famille; les colonnes ci-dessous disent ce qu'il en dérivera.

*Certains systèmes libellent `PV_SIGNIFICATION_DESIGNEE` « procès-verbal de notification ». L'art. 120
C.p.c. parle de signification : la notification est le genre, la signification l'espèce. Employer le
code du système, et le terme exact du Code dans la prose.*

**Les ancrages légaux nomment, ils n'argumentent pas.** L'article cité sert à reconnaître un
document, jamais à fonder une prétention : cela relève de `recherche-juridique`.

---

## Actes de procédure — catégorie dérivée `procédure`

| Code | Libellé | Ancrage |
|---|---|---|
| `PROC_DEM_INTRO` | Demande introductive d'instance | art. 100, 107 C.p.c. |
| `PROC_AVIS_ASSIGN` | Avis d'assignation | art. 145 C.p.c. |
| `PROC_DEM_INSTANCE` | Demande en cours d'instance | art. 101 C.p.c. |
| `PROC_PROTOCOLE` | Protocole de l'instance | art. 148 C.p.c. |
| `PROC_MOYEN_PRELIM` | Moyen préliminaire | art. 166 à 168 C.p.c. (dénonciation; déclinatoire; irrecevabilité) |
| `PROC_DEFENSE` | Défense écrite | art. 170 C.p.c. |
| `PROC_EXPOSE_SOMMAIRE` | Exposé sommaire des éléments de contestation | art. 148 al. 2 (5°), 170 al. 2 C.p.c. |
| `PROC_DEM_RECONV` | Demande reconventionnelle | art. 172 C.p.c. |
| `PROC_INTERVENTION` | Intervention volontaire ou forcée | art. 184 C.p.c. |
| `PROC_DECL_SERMENT` | Déclaration sous serment | art. 99, 105 C.p.c. |
| `PROC_DEM_INSCRIPTION` | Demande d'inscription pour instruction et jugement | art. 173 C.p.c. |
| `PROC_DECL_APPEL` | Déclaration d'appel | art. 352, 353 C.p.c. (l'art. 358 en régit la signification) |
| `PROC_AUTRE` | Autre acte de procédure | art. 99 C.p.c. |

**Le discriminant décisif est le numéro de dossier de cour.** Un acte de procédure qui n'en porte
pas est presque toujours un **projet non déposé** : il n'a jamais accédé au caractère public de
l'art. 11 C.p.c., il relève du travail préparatoire, et il se qualifie en conséquence au temps 3.

Un acte de procédure ne prouve rien par lui-même : il allègue. Ne jamais lui attribuer de moyen de
preuve.

## Jugements — catégorie dérivée `jugement`

| Code | Libellé | Ancrage |
|---|---|---|
| `JUG_JUGEMENT` | Jugement de première instance | — |
| `JUG_ARRET` | Arrêt de la Cour d'appel | art. 389 C.p.c. |
| `JUG_ORDONNANCE` | Ordonnance | — |

Une citation neutre au visage du document s'authentifie (voir le SKILL.md, « Ce que les sources de
droit ajoutent au tri »). Un document qui se présente comme un jugement sans citation neutre, sans
numéro de dossier de cour ou sans signature est un **projet** ou un extrait — le signaler.

## Procès-verbaux

| Code | Libellé | Catégorie dérivée | Ancrage |
|---|---|---|---|
| `PV_SIGNIFICATION` | Procès-verbal de signification — huissier | `procès_verbal_signification` | art. 119 C.p.c. |
| `PV_SIGNIFICATION_DESIGNEE` | Procès-verbal de signification par une personne désignée par l'huissier | `procès_verbal_signification` | art. 120 C.p.c. |
| `PV_AUDIENCE` | Procès-verbal d'audience | `procès_verbal_audience` | — |
| `PV_AUDIENCE_JUGEMENT` | Procès-verbal d'audience **portant jugement** | `procès_verbal_audience` | — |

`PV_AUDIENCE_JUGEMENT` est la sous-nature à repérer : un jugement rendu à l'audience fait courir
les délais d'appel. **Le signaler; ne jamais calculer le délai.**

## Transcriptions — catégorie dérivée `transcription`

| Code | Libellé |
|---|---|
| `TRANS_INTERROGATOIRE` | Notes sténographiques d'interrogatoire |
| `TRANS_AUDIENCE` | Notes sténographiques d'audience |

## Correspondance — catégorie dérivée `correspondance`

| Code | Libellé | Ancrage |
|---|---|---|
| `CORR_MISE_DEMEURE` | Mise en demeure | art. 1595 C.c.Q. |
| `CORR_CONFRERE` | Lettre ou courriel au confrère | — |
| `CORR_CLIENT` | Lettre ou courriel au client | — |
| `CORR_TRIBUNAL` | Lettre au tribunal ou au greffe | — |
| `CORR_EXPERT` | Communication avec un expert | — |
| `CORR_TIERS` | Correspondance avec un tiers | — |
| `CORR_AUTRE` | Autre correspondance | — |

**L'identité du destinataire commande la sous-nature, et la sous-nature commande le régime.** Une
lettre au client relève du secret professionnel; une lettre au confrère est généralement
confidentielle et peut porter un privilège de règlement; une lettre au greffe est souvent versée au
dossier. Établir le destinataire réel — les copies conformes en font partie — avant de qualifier.

Une chaîne de courriels peut contenir plusieurs auteurs et plusieurs régimes. Qualifier le message
analysé, signaler les autres, et retenir le régime le plus élevé de l'ensemble transmis.

## Pièces et preuve

| Code | Libellé | Catégorie dérivée |
|---|---|---|
| `PIECE_COMMUNIQUEE` | Pièce cotée, notifiée et déposée | `pièce` |
| `PREUVE_CONTRAT` | Contrat, entente, quittance | `preuve` |
| `PREUVE_COURRIEL` | Courriel ou message produit comme preuve | `preuve` |
| `PREUVE_FACTURE` | Facture d'un tiers | `preuve` |
| `PREUVE_RELEVE` | Relevé, état de compte | `preuve` |
| `PREUVE_PHOTO` | Photographie | `preuve` |
| `PREUVE_RAPPORT_EXPERT` | Rapport d'expertise | `preuve` |
| `PREUVE_AUTRE` | Autre élément de preuve | `preuve` |

**`PIECE_COMMUNIQUEE` ne se retient que si le document porte la marque de sa cotation** — une cote
(P-1, D-3, PC-2), un avis de notification, une mention de dépôt. C'est la sous-nature qui emporte
la présomption de caractère public : elle ne se présume jamais de l'absence de marque contraire.

Un document peut être à la fois un contrat et une pièce cotée. Retenir `PIECE_COMMUNIQUEE` quand la
cotation est établie, et signaler au temps 3 tout indice de régime protégé qui subsisterait — c'est
le signalement de renonciation possible.

## Documents du cabinet

| Code | Libellé | Catégorie dérivée |
|---|---|---|
| `CAB_MANDAT` | Mandat, convention d'honoraires | `mandat` |
| `CAB_FACTURE` | Note d'honoraires du cabinet | `facture` |
| `CAB_DEBOURSE` | Pièce justificative de déboursé | `déboursé` |
| `CAB_MEMO` | Mémorandum ou note interne | `autre` |

`CAB_MEMO` couvre le travail préparatoire du cabinet : analyse, théorie de la cause, plan
d'argumentation, projet annoté. C'est la sous-nature dont le régime est presque toujours le plus
élevé du lot.

## Indéterminé

| Code | Libellé | Catégorie dérivée |
|---|---|---|
| `NON_DETERMINE` | Nature indéterminée | `autre` |

**`NON_DETERMINE` est un résultat honnête, pas un échec.** Le retenir plutôt que de forcer un
document dans la sous-nature la moins improbable, et dire ce qui manque pour trancher : le texte
d'une page numérisée, l'en-tête d'un courriel, la page de signature, une cote.

---

## Départager les cas voisins

| Confusion fréquente | Ce qui tranche |
|---|---|
| `PROC_*` sans dépôt / `CAB_MEMO` | Un projet annoté ou commenté par l'avocat est du travail préparatoire, quoi que dise son titre |
| `JUG_JUGEMENT` / `PV_AUDIENCE_JUGEMENT` | Le jugement est un document autonome signé; le procès-verbal relate l'audience et **porte** le jugement |
| `CORR_MISE_DEMEURE` / `CORR_CONFRERE` | La mise en demeure somme d'exécuter dans un délai et annonce la sanction du défaut; une lettre qui discute sans sommer n'en est pas une |
| `PREUVE_COURRIEL` / `CORR_*` | Un courriel du cabinet est de la correspondance; un courriel entre tiers, produit pour établir un fait, est de la preuve |
| `PREUVE_CONTRAT` / `PIECE_COMMUNIQUEE` | La cotation, lorsqu'elle est marquée, l'emporte |
| `PREUVE_RAPPORT_EXPERT` / `CORR_EXPERT` | Le rapport conclut et est destiné au tribunal; l'échange avec l'expert est de la correspondance, et son régime est plus élevé tant que le rapport n'est pas communiqué |
| `PREUVE_FACTURE` / `CAB_FACTURE` / `CAB_DEBOURSE` | L'émetteur : un tiers, le cabinet, ou un fournisseur du cabinet |
