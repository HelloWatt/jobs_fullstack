# Challenge Hello Watt

Vous cherchez un job/stage ? Découvrez [nos offres d'emplois](https://hello-watt.welcomekit.co/).

## Votre mission

Votre objectif est de mettre en place un dashboard simplifié de diagnostic en un clic.
Le projet possède déjà une base de données contenant les informations de consommation d'électricité de 5000 clients depuis 2015.
Une page d'accueil existe déjà, listant l'ensemble des clients dans la base de données.

Vous devez au minimum:

- Afficher la courbe de consommation de l'année passée
- Identifier si le client a un chauffage électrique ou non (hint: en hiver la consommation électrique est bien plus importante en cas de chauffage électrique)
- Détecter un dysfonctionnement: cela se traduit par un changement brusque par rapport à l'année passé. En cas de dysfonctionnement, indentifier le mois et l'année où le dysfonctionnement est survenu.
- Mettre à jour les colonnes Heating et Health de la liste des clients (/admin/clients), qui indiquent s'il y a un chauffage électrique et si un dysfonctionnement a été détecté.

Les administrateurs peuvent visualiser la liste de clients depuis /admin/clients.

Une partie de nos utilisateurs est sur mobile.

La base de donnée de production contiendra des centaines de milliers de clients.

Vous êtes libre de changer complétement l'application. Impressionez-nous !

## Mise en place

- Cloner ce dépo (ne pas en faire un fork)
- Installer les dépendances se trouvant dans requirements.txt
- Démarrer le serveur: $ python manage.py runserver


Le projet contient déjà les modèles de la base de données et quelques tests.
Vous trouverez dans l'app dashboard un dossier fixtures et metadata. Les fixtures sont déjà chargées en base de données, vous n'aurez donc probablement pas besoin d'y toucher.
Le dossier metadata contient des informations additionnelles sur les clients, il est là uniquement pour que vous puissiez tester vos résultats avec la "réalité".

## Librairies à votre disposition

Seul Django et Black (outil de formatage du code) sont listés en dépendances Python.
En front eva-icons est installée (https://github.com/akveo/eva-icons#how-to-use).

Vous êtes libre d'installer d'autres dépendances si besoin, que ce soit des dépendances Python (drf, ...), javascript (React, Vue, ...), css (bootstrap, tailwind, ...).

## Une fois terminé

Une fois que vous avez terminé, merci de contacter votre correspondant chez Hello Watt.

Envoyez vos résultats :
- Sous la forme d'un lien Github (ou Gitlab, ou autre) vers votre projet. **Attention, votre projet doit être privé**, partagez-le uniquement avec votre correspondant Hello Watt.
- Par email avec le zip du projet (Cela ne vous exempt pas de commit vos changements réguliérement. N'oubliez pas le dossier .git dans le zip).
