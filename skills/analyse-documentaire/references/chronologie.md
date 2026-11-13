# La chronologie

Tirer d'un lot la suite des événements, une ligne par événement, chacune rattachée à ce qui
l'établit. À lire en mode chronologie.

## Ce qu'est un événement

Un fait daté, ou datable, qui a eu lieu : une signature, un envoi, une réception, un paiement, une
livraison, une mise en demeure, une signification, une audience, un jugement. **Un document n'est
pas un événement** — c'est une source. Le contrat du 4 mars est la source de l'événement « [A] et
[B] signent le contrat, 4 mars 2025 »; le courriel du 12 novembre est la source de « [A] écrit à
[B] », et parfois d'un second événement qu'il relate — « [A] affirme que la livraison a eu lieu le
2 » —, qui porte alors un autre statut.

Trois sortes d'événements coexistent dans un lot, et la chronologie les distingue à chaque ligne :

| Sorte | Ce que c'est | Exemple | Statut du fait |
|---|---|---|---|
| **Constaté par la pièce** | La pièce est elle-même l'événement, ou l'atteste par sa nature | Le contrat signé, le procès-verbal de signification, le jugement | **Établi** — sous réserve de la force probante de la pièce |
| **Relaté par la pièce** | La pièce rapporte que quelque chose a eu lieu | Un courriel qui dit « comme convenu au téléphone hier » | **Rapporté** — c'est la déclaration de l'auteur, pas le fait |
| **Déduit** | Aucune pièce ne le porte; il s'infère de deux autres | Une livraison entre la commande et la facture | **Déduit** — à marquer comme tel, jamais à présenter comme établi |

Le statut du fait est celui de `redaction-juridique` : établi, rapporté, absent. La chronologie y
ajoute « déduit », qui est un absent honnête.

## Comment dater

**La date propre du document, jamais celle du fichier.** La date de création, de modification, de
numérisation ou de téléversement d'un fichier n'est pas la date de l'événement; elle est parfois
postérieure de plusieurs années. Un courriel se date par son en-tête, avec son fuseau horaire quand
il compte; une lettre par sa date dactylographiée, et par le cachet ou l'accusé quand la réception
importe; un contrat par sa date de signature — et quand il en porte plusieurs, par la dernière, en
le disant.

**Trois précisions de date, et on écrit laquelle** :

| Précision | Écriture | Quand |
|---|---|---|
| Exacte | `2025-11-12` | La pièce porte la date |
| Approximative | `~2025-11` · `avant 2025-11-12` · `entre 2025-11-04 et 2025-11-12` | La date se déduit d'un encadrement |
| Inconnue | `[DATE]` | Rien ne la fixe; la ligne reste, le trou se voit |

Ne jamais arrondir une date approximative en date exacte pour que la table soit propre. Une
chronologie qui a l'air complète et qui ne l'est pas est pire qu'une chronologie à trous.

**Les heures** ne s'écrivent que si elles comptent — un courriel envoyé avant ou après une
signification le même jour, une offre reçue avant l'audience. Alors le fuseau se dit.

## Les trous et les contradictions

**Un trou** est un intervalle où quelque chose a nécessairement eu lieu et qu'aucune pièce ne
couvre : entre la mise en demeure et la demande introductive, entre la commande et la facture. Le
marquer d'une ligne propre — « [TROU] entre le 20 novembre et le 4 mars : aucune pièce » —, parce
que c'est là que l'avocat cherchera, et parce qu'un trou est souvent l'endroit où la partie adverse
a une pièce qu'on n'a pas.

**Une contradiction** est deux pièces qui datent différemment le même événement, ou qui relatent
des faits incompatibles. Elle ne se résout pas dans la chronologie : les deux versions y figurent,
face à face, avec leurs sources, et la contradiction est signalée en pied. Choisir une version
serait décider le litige.

## Ce que la chronologie ne fait pas

Elle **ne qualifie pas** les faits en droit — savoir si la mise en demeure du 20 novembre a
interrompu la prescription relève de `recherche-juridique`. Elle **ne calcule pas** les délais que
les événements font courir — c'est `calendrier-procedural`, et la chronologie lui fournit les
ancrages. Elle **ne raconte pas** : une chronologie est une table, pas un récit; le récit, s'il en
faut un, se rédige ensuite à partir d'elle, et c'est `redaction-juridique`.

Elle ne comble aucun trou par vraisemblance. Ce qui n'est pas dans une pièce n'est pas dans la
chronologie, sauf marqué « déduit ».

## Gabarit

Une ligne par événement, dans l'ordre des dates; les événements de date inconnue à la place que la
déduction leur donne, marqués. En pied : les trous, les contradictions, et les pièces du lot qui
n'ont produit aucun événement — elles existent, et il faut dire pourquoi elles n'y sont pas.

    CHRONOLOGIE — [dossier ou question], dressée le [date], sur [n] pièces

    | Date | Événement | Source | Statut |
    |---|---|---|---|
    | 2025-03-04 | [A] et [B] signent le contrat de vente | P-1, p. 12 (signatures) | Établi |
    | ~2025-10 | Livraison du bien | Déduit de P-1 (livraison « dans les six mois ») et P-4 (facture du 2025-10-30) | Déduit |
    | 2025-11-12 | [A] écrit à [B] : « comme convenu au téléphone hier » | P-3, courriel 1 | Établi (l'envoi) |
    | 2025-11-11 | Conversation téléphonique [A]–[B] | P-3, courriel 1 — relatée par [A] | Rapporté |
    | 2025-11-20 | [A] met [B] en demeure | P-2 | Établi |
    | [TROU] | Entre le 2025-11-20 et le 2026-03-04 : aucune pièce | — | — |
    | 2026-03-04 | Demande introductive d'instance signifiée à [B] | Procès-verbal de signification | Établi |

    Contradictions : P-3 (courriel 4) date la livraison du 2025-10-28; P-4 la date du 2025-10-30.
    Pièces sans événement : P-5 (relevé bancaire — aucun mouvement pertinent identifié).

L'ordre des lignes suit la date de l'événement, non celle de la source : la conversation du 11
novembre précède le courriel du 12 qui la relate, même si c'est le courriel qu'on lit.
