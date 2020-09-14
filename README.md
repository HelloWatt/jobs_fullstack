# Challenge Hello Watt

Vous cherchez un job/stage ? Découvrez [nos offres d'emplois](https://hello-watt.welcomekit.co/).

## Votre mission

Votre objectif est de mettre en place un dashboard simplifié de diagnostic énergétique.
Le projet possède déjà une base de données contenant les informations de consommation d'électricité de 5000 clients depuis 2015.

Le site comporte actuellement 3 pages:
- Une page d'accueil `/`: Permet de rechercher les clients (actuellement la recherche ne fonctionne que par id)
- Une page client `/consumption/<id>`: Affiche la courbe de consommation de l'année des 12 derniers mois. Et informe en cas de chauffage électrique ou de dysfonctionnement. (vide pour le moment)
- Une page admin `/admin/clients`: Une liste de clients accessible uniquement au staff qui permet de rapidement voir les clients avec un chauffage électrique ou un dysfonctionement. 

Votre mission, si vous l'acceptez est d'ajouter ce qui manque sur ces pages. C'est à dire:

- Sur le dashboard `/consumption/<id>`:
    - Afficher la courbe de consommation des 12 derniers mois.
    - Identifier et afficher si le client a un chauffage électrique ou non (indice: en hiver la consommation électrique est bien plus importante en cas de chauffage électrique).
    - Détecter et afficher un dysfonctionnement: cela se traduit par un changement brusque de la consommation d'un mois à l'autre. En cas de dysfonctionnement, indentifier le mois et l'année où le dysfonctionnement est survenu.
- Sur le dashboard `/admin/clients`:
    - Mettre à jour les colonnes `Heating` et `Health` de la liste des clients (`/admin/clients`).
- Sur l'accueil `/`:
    - (Optionnel) Rechercher par nom et/ou prénom

Quelques informations sur nos utilisateurs:
- Une partie de nos utilisateurs est sur mobile.
- La base de donnée de production contiendra des dizaines de milliers de clients.

Pour l'exercice n'importe quel utilisateur peut accéder au dashboard de tout le monde. Nous n'attendons pas qu'un système d'authentification et d'autorisation soit ajouté.

Vous êtes libre de changer complètement l'application. Amusez-vous !

## Mise en place

- Si vous n'êtes pas familier avec Django prenez un peu de temps pour lire le [guide de démarrage](https://www.djangoproject.com/)
- Cloner ce dépo (ne pas en faire un fork)
- Installer les dépendances se trouvant dans requirements.txt
- Démarrer le serveur: `$ python manage.py runserver`

Vous trouverez dans l'app dashboard un dossier fixtures et metadata.
Les fixtures sont déjà [chargées](https://docs.djangoproject.com/en/3.1/howto/initial-data/) en base de données, vous n'aurez donc probablement pas besoin d'y toucher.
Le dossier metadata contient des informations additionnelles sur les clients, il est là uniquement pour que vous puissiez tester vos résultats avec la "réalité".

## Librairies à votre disposition

Seul [Django](https://www.djangoproject.com/) et [black](https://github.com/psf/black) sont listés en dépendances Python.
En front [eva-icons](https://github.com/akveo/eva-icons#how-to-use) est installée.

Vous êtes libre d'installer d'autres dépendances si besoin,
que ce soit des dépendances Python (drf, ...),
javascript (React, Vue, Svelte, ...),
css (tailwindcss, bootstrap, ...).

## Une fois terminé

Une fois que vous avez terminé, envoyez votre projet à votre correspondant chez Hello Watt.

Envoyez vos résultats :
- Sous la forme d'un lien Github ou Gitlab vers votre projet. **Attention, votre projet doit être privé**, partagez-le uniquement avec votre correspondant Hello Watt.
- Par email avec le zip du projet, **ce zip doit contenir l'historique git du projet !** (Veillez à ce que le dossier .git soit présent dans l'archive pour que nous ayons accès à l'historique)
