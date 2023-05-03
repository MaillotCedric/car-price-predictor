from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from app.models import Carburant, Categorie, Couleur, IntervalleProduction, Marque, Modele

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
