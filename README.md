# Peer programming

## Votre mission

Notre objectif est d'ensemble mettre en place un dashboard simplifié de diagnostic énergétique. On reprend un projet commencé par un autre développeur, il y a donc déjà une base de code.
Le projet possède déjà une base de données contenant les informations de consommation d'électricité de 5000 clients depuis 2015.

Les fonctionnalités attendu sont réparties sur 2 pages:
- Une page d'accueil `/`: Permet de rechercher les clients (actuellement la recherche ne fonctionne que par id)
- Une page client `/consumption/<id>`: Affiche la courbe de consommation de l'année des 12 derniers mois, et informe en cas de chauffage électrique ou de dysfonctionnement. (vide pour le moment)

Notre mission est d'ajouter ce qui manque sur ces pages. C'est à dire:

- Sur le dashboard `/consumption/<id>`:
    - Afficher la courbe de consommation des 12 derniers mois.
    - Afficher si le client a un chauffage électrique ou non.
    - Détecter et afficher un dysfonctionnement: cela se traduit par un changement brusque de la consommation d'un mois à l'autre.
- Sur la page d'accueil `/`:
    - Rechercher par nom et/ou prénom

## Tip

Le dossier `metadata` contient des informations additionnelles sur les clients, il est là pour que nous puissions confronter nos résultats avec la "réalité".

## Librairies à votre disposition

Seul [Django](https://www.djangoproject.com/) et [black](https://github.com/psf/black) sont listés en dépendances Python.

Vous êtes libre d'installer d'autres dépendances si besoin,
que ce soit des dépendances Python (drf, ...),
javascript (React, Vue, Svelte, ...),
css (tailwindcss, bootstrap, ...).
