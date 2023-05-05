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

Install a virtual environment :

- Windows :

    `py -m venv .env`

- Linux or Mac OS :

    `python3 -m venv .env or python -m venv .env`

Activate the virtual environment :

- Windows :

    `.env\Scripts\activate`

- Linux or Mac OS :

    `source .env/bin/activate`

Install packages (Django, ...) :

    `pip install -r requirements.txt`

- Hide the key to the castle :

    - Create the safe :

        Inside project folder, create a file called `.env`

    - Generate the key :

        a. Run the following command in the terminal of your Django project

        . Windows :

        `py manage.py shell`

        . Linux or Mac OS :

        `python3 manage.py shell or python manage.py shell`

        b. Import the key generator function

        Run the following command and hit Enter :

        `from django.core.management.utils import get_random_secret_key`

        c. Generate a random key

        On the next line we can now use the function to generate the secret key

        `print(get_random_secret_key())`

    - Hide the key

        Copy the generated key

        In the `.env` file, declare a SECRET_KEY variable as follows

        `SECRET_KEY=<generated key>`

    *The castle is well-protected now :)*

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

## Modèle conceptuel de données

![Modèle conceptuel de données](/doc/Modele%20conceptuel%20de%20donn%C3%A9es.PNG "Modèle conceptuel de données")

## Modèle physique de données

![Modèle physique de données](/doc/Mod%C3%A8le%20physique%20de%20donn%C3%A9es.PNG "Modèle physique de données")

## API REST

| URI                                | Autorisation | Méthode | Données | Description                                                  |
| ---------------------------------- | ------------ | ------- | ------- | ------------------------------------------------------------ |
| /api/carburants/                   | No Auth      | GET     | None    | Liste des types de carburant                                 |
| /api/categories/                   | No Auth      | GET     | None    | Liste des catégories de véhicule                             |
| /api/couleurs/                     | No Auth      | GET     | None    | Liste de couleurs                                            |
| /api/intervalles_production/       | No Auth      | GET     | None    | Liste des intervalles de production (Les années de production d'un véhicule ont été regroupées par tranches de 10 ans) |
| /api/ marques/                     | No Auth      | GET     | None    | Liste des marques de voiture                                 |
| /api/modeles/                      | No Auth      | GET     | None    | Liste des modèles de voiture                                 |
| /api/modeles?id_marque=\<id_marque\> | No Auth      | GET     | None    | Liste des modèles existants pour une marque de voiture       |
| /api/ouvertures/                   | No Auth      | GET     | None    | Liste des types d'ouvertures (2-3 portes, ...)               |
| /api/roues_motrices/               | No Auth      | GET     | None    | Liste des types de traction d'un véhicule                    |
| /api/transmissions/                | No Auth      | GET     | None    | Liste des types de transmission d'un véhicule                |
| /api/voitures/                     | No Auth      | GET     | None    | Liste des voitures sur lesquelles on a effectué une prédiction de prix |
| /api/predire/ | No Auth | POST | [mileage, model, ...] | Renvoie une prédiction (prix estimé) en récupérant les données du formulaire |
