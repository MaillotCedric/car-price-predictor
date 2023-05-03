# Car price predictor

## Contexte du projet

Le client de votre entreprise est un concessionnaire de voiture d'occasion. Il souhaite mettre en place un site internet à visé de ses prospects/clients leur permettant de réaliser une estimation de coût de rachat de leur véhicule.

En tant que data scientist, vous devrez réaliser les taches suivantes :

- Analyse et nettoyage des données
- Modélisation du problème
- Optimisation des paramètres
- Réalisation de l'application pour rendre le modèle exploitable par l'utilisateur final
​

De votre travail vous pourrez déduire une valeur du véhicule à la revente.Le prix indiqué au client final devra prendre en compte sa marge de 30%.

Contrainte technique :

L'application réalisée devra utiliser en technologie front un framework js moderne.

## Dataset

[Car Price Prediction Challenge](https://www.kaggle.com/datasets/deepcontractor/car-price-prediction-challenge)

## Installation

Install the PostgreSQL database connection package

- Windows :

    pip install psycopg2

- Linux or Mac OS :

    pip install psycopg2-binary

Create database :

- Database settings :

    - Name : `<database name>`
    - User : `<database user name> (default : postgres)`
    - Password : `<database password>`

Inside project folder, create a file called `.env``

Update project/settings.py (source) :

``` python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER_NAME"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

Update project/.env :

```
DB_NAME=<database name>
DB_USER_NAME=<database user name> (default : postgres)
DB_PASSWORD=<database password>
```

Make the first migrations :

- Windows :

    `py manage.py makemigrations`

    `py manage.py migrate`

- Linux or Mac OS :

    `python3 manage.py migrate or python manage.py migrate`

    `python3 manage.py makemigrations or python manage.py makemigrations`

    `python3 manage.py migrate or python manage.py migrate`

Create superuser :

- Windows :

    `py manage.py init_local_dev`

- Linux or Mac OS :

    `python3 manage.py init_local_dev or python manage.py init_local_dev`
