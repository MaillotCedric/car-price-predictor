from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from app.models import Carburant, Categorie, Couleur, IntervalleProduction, Marque, Modele, Ouverture, RoueMotrice, Transmission, Voiture

class UsersListeSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_active"]

class UsersDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CarburantsListeSerializer(ModelSerializer):
    class Meta:
        model = Carburant
        fields = "__all__"

class CategoriesListeSerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"

class CouleursListeSerializer(ModelSerializer):
    class Meta:
        model = Couleur
        fields = "__all__"

class IntervallesProductionListeSerializer(ModelSerializer):
    class Meta:
        model = IntervalleProduction
        fields = "__all__"

class MarquesListeSerializer(ModelSerializer):
    class Meta:
        model = Marque
        fields = "__all__"

class ModelesListeSerializer(ModelSerializer):
    class Meta:
        model = Modele
        fields = "__all__"

class OuverturesListeSerializer(ModelSerializer):
    class Meta:
        model = Ouverture
        fields = "__all__"

class RouesMotricesListeSerializer(ModelSerializer):
    class Meta:
        model = RoueMotrice
        fields = "__all__"

class TransmissionsListeSerializer(ModelSerializer):
    class Meta:
        model = Transmission
        fields = "__all__"

class VoituresListeSerializer(ModelSerializer):
    class Meta:
        model = Voiture
        fields = "__all__"
