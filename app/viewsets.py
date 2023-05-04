from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from app.mixins import MultipleSerializerMixin, EnablePartialUpdateMixin
from app.serializers import UsersListeSerializer, UsersDetailsSerializer,CarburantsListeSerializer, CategoriesListeSerializer, CouleursListeSerializer, IntervallesProductionListeSerializer, MarquesListeSerializer, ModelesListeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from app.models import Carburant, Categorie, Couleur, IntervalleProduction, Marque, Modele

class ReadUpdateModelViewSet(ModelViewSet):
    http_method_names = ["get", "put", "patch"]

class CreateModelViewSet(ModelViewSet):
    http_method_names = ["post"]

# class UsersAPIViewset(MultipleSerializerMixin, ModelViewSet):
# class UsersAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
class UsersAPIViewset(MultipleSerializerMixin, ReadUpdateModelViewSet):
# class UsersAPIViewset(MultipleSerializerMixin, ReadUpdateModelViewSet, EnablePartialUpdateMixin):
    serializer_class = UsersListeSerializer
    details_serializer_class = UsersDetailsSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action in ["deactivate", "activate"]:
            self.permission_classes = [IsAuthenticated,]
        elif self.action in ["retrieve"]:
            self.permission_classes = [IsAuthenticatedOrReadOnly,]

        return super().get_permissions()

    def get_queryset(self):
        queryset = User.objects.all()

        return queryset

    # @action(detail=True, methods=["patch"], permission_classes = [IsAuthenticated])
    @action(detail=True, methods=["patch"])
    def deactivate(self, request, pk):
        self.get_object().deactivate()

        return Response()

    # @action(detail=True, methods=["patch"],  permission_classes = [IsAuthenticated])
    @action(detail=True, methods=["patch"])
    def activate(self, request, pk):
        self.get_object().activate()

        return Response()

class CarburantsAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = CarburantsListeSerializer

    def get_queryset(self):
        queryset = Carburant.objects.all()

        return queryset

class CategoriesAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = CategoriesListeSerializer

    def get_queryset(self):
        queryset = Categorie.objects.all()

        return queryset

class CouleursAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = CouleursListeSerializer

    def get_queryset(self):
        queryset = Couleur.objects.all()

        return queryset

class IntervallesProductionAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = IntervallesProductionListeSerializer

    def get_queryset(self):
        queryset = IntervalleProduction.objects.all()

        return queryset

class MarquesAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = MarquesListeSerializer

    def get_queryset(self):
        queryset = Marque.objects.all()

        return queryset

class ModelesAPIViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):
    serializer_class = ModelesListeSerializer

    def get_queryset(self):
        queryset = Modele.objects.all()
        id_marque = self.request.GET.get("id_marque")

        if id_marque is not None:
            queryset = queryset.filter(id_marque = id_marque)

        return queryset
