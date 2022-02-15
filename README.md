# API_FLASK
Commencer
Cet api permet de gérer une bibliothèque en listant les livres et les catégories

Installation des Dépendances
Python 3.9.6
pip 21.1.3 from c:\users\acer\appdata\local\programs\python\python39\lib\site-packages\pip (python 3.9)
Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme python docs

Dépendances de PIP
Pour installer les dépendances, ouvrez le dossier /Documentation et exécuter la commande suivante:

pip freeze > requirements.txt
Nous passons donc à l'installation de tous les packages se trouvant dans le fichier requirements.txt.

clé de Dépendances
Flask est un petit framework web Python léger, qui fournit des outils et des fonctionnalités utiles qui facilitent la création d’applications web en Python.

SQLAlchemy est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.

Démarrer le serveur
Pour démarrer le serveur sur Linux ou Mac, executez:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Pour le démarrer sur Windows, executez:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run
API REFERENCE
Getting starter

URL de base : à l’heure actuelle, cette application ne peut être exécutée que localement et n’est pas hébergée en tant qu’URL de base. L’application backend est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.

Type d'erreur
Les erreurs sont renvoyées sous forme d'objet au format Json: { "success":False "error": 400 "message":"Ressource non disponible" }

L'API vous renvoie 4 types d'erreur: . 400: Bad request ou ressource non disponible . 500: Internal server error . 404: Not found

Endpoints
. ## GET/livres

GENERAL:
    Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 

 {
 {
    "livres": [
        {
            "categories_id": 4,
            "code ISBN": "2708700851",
            "date publication": "Sun, 13 Feb 1955 00:00:00 GMT",
            "nom auteur": "bernard DADIE",
            "nom editeur": "Presence africaine",
            "titre": "pagne noir"
        },
        {
            "categories_id": 1,
            "code ISBN": "741000",
            "date publication": "Thu, 15 Feb 2052 00:00:00 GMT",
            "nom auteur": "hiro",
            "nom editeur": "ponyon",
            "titre": "fairy tail"
        },
        {
            "categories_id": 2,
            "code ISBN": "2711",
            "date publication": "Mon, 04 May 1998 00:00:00 GMT",
            "nom auteur": "benjamin",
            "nom editeur": "telemundo",
            "titre": "coeur brise"
        },
        {
            "categories_id": 1,
            "code ISBN": "7400",
            "date publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "nom auteur": "james",
            "nom editeur": "starz",
            "titre": "power_ghost"
        },
        {
            "categories_id": 3,
            "code ISBN": "52000",
            "date publication": "Mon, 14 Oct 1996 00:00:00 GMT",
            "nom auteur": "nick",
            "nom editeur": "Gallimard",
            "titre": "nicky larson"
        },
        {
            "categories_id": 4,
            "code ISBN": "54000",
            "date publication": "Fri, 01 Dec 2056 00:00:00 GMT",
            "nom auteur": "robert",
            "nom editeur": "Flammarion",
            "titre": "tour du monde en 80 jours"
        }
    ],
    "success": true,
    "total": 6
}

.##Get/livres/id GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

{
    "selected_books": {
        "categories_id": 1,
        "code ISBN": "7400",
        "date publication": "Thu, 10 Feb 2022 00:00:00 GMT",
        "nom auteur": "james",
        "nom editeur": "starz",
        "titre": "power_ghost"
    },
    "selected_id": 3,
    "success": true
}
. ## DELETE/livres/id

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.
  {
    "deleted_book": {
        "categories_id": 1,
        "code ISBN": "741000",
        "date publication": "Thu, 15 Feb 2052 00:00:00 GMT",
        "nom auteur": "hiro",
        "nom editeur": "ponyon",
        "titre": "fairy tail"
    },
    "deleted_id": 4,
    "success": true,
    "total": 5
}
. ##PATCH/livres/id GENERAL: Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre. Il retourne un livre mis à jour.

EXEMPLE.....Avec Patch

  {
    "new_livres": {
        "categories_id": 1,
        "code ISBN": "7452100",
        "date publication": "Tue, 15 Feb 2022 00:00:00 GMT",
        "nom auteur": "gil",
        "nom editeur": "présence noire",
        "titre": "romain"
    },
    "success": true,
    "updated_id_book": 1

. ## GET/categories

  GENERAL:
      Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles.

   {
    "livres": [
        {
            "id": 1,
            "libelle categorie": "Fiction"
        },
        {
            "id": 3,
            "libelle categorie": "Policier"
        },
        {
            "id": 4,
            "libelle categorie": "Aventure"
        },
        {
            "id": 2,
            "libelle categorie": "romance"
        },
        {
            "id": 5,
            "libelle categorie": "necromancie"
        },
        {
            "id": 6,
            "libelle categorie": "horreur"
        }
    ],
    "success": true,
    "total": 6
}

. ## DELETE/categories/id

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.
{
    "deleted_categorie": {
        "id": 5,
        "libelle categorie": "necromancie"
    },
    "deleted_id": 5,
    "success": true,
    "total": 5
}
. ##PATCH/categories/id GENERAL: Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie. Il retourne une nouvelle categorie avec la nouvelle valeur.

{
    "new_categorie": {
        "id": 2,
        "libelle categorie": "horreur"
    },
    "success": true,
    "updated_id_categorie": 2
}

.##GET/categories/id/livres GENERAL: Cet endpoint permet de lister les livres appartenant à une categorie donnée. Il renvoie la classe de la categorie et les livres l'appartenant.

 {
    "livres": [
        {
            "categories_id": 1,
            "code ISBN": "7400",
            "date publication": "Thu, 10 Feb 2022 00:00:00 GMT",
            "nom auteur": "james",
            "nom editeur": "starz",
            "titre": "power_ghost"
        },
        {
            "categories_id": 1,
            "code ISBN": "7452100",
            "date publication": "Tue, 15 Feb 2022 00:00:00 GMT",
            "nom auteur": "gil",
            "nom editeur": "présence noire",
            "titre": "romain"
        }
    ],
    "success": true,
    "total": 2
}
.##Get/categories/id GENERAL: Cet endpoint permet de récupérer les informations d'une catégorie particulière s'il existe par le biais de l'ID.
{
    "selected_categories": {
        "id": 1,
        "libelle categorie": "Fiction"
    },
    "selected_id": 1,
    "success": true
}
