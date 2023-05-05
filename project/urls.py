"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.viewsets import UsersAPIViewset, CarburantsAPIViewset, CategoriesAPIViewset, CouleursAPIViewset, IntervallesProductionAPIViewset, MarquesAPIViewset, ModelesAPIViewset, OuverturesAPIViewset, RouesMotricesAPIViewset, TransmissionsAPIViewset, VoituresAPIViewset
# from app.views import login_

router = routers.SimpleRouter()

router.register("users", UsersAPIViewset, basename="users")
router.register("carburants", CarburantsAPIViewset, basename="carburants")
router.register("categories", CategoriesAPIViewset, basename="categories")
router.register("couleurs", CouleursAPIViewset, basename="couleurs")
router.register("intervalles_production", IntervallesProductionAPIViewset, basename="intervalles_production")
router.register("marques", MarquesAPIViewset, basename="marques")
router.register("modeles", ModelesAPIViewset, basename="modeles")
router.register("ouvertures", OuverturesAPIViewset, basename="ouvertures")
router.register("roues_motrices", RouesMotricesAPIViewset, basename="roues_motrices")
router.register("transmissions", TransmissionsAPIViewset, basename="transmissions")
router.register("voitures", VoituresAPIViewset, basename="voitures")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("app.urls")),
    path("api/", include(router.urls)),
    # path("login/", login_, name="login"),
]