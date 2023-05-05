from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView

@login_required(login_url="login")
def home(request):
    return render(request, "home.html", {})

def login_(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect("home")
        else:
            messages.warning(request, "Username and/or password not valid")

            return redirect("login")
    else:
        return render(request, "login.html", {})

def logout_(request):
    logout(request)
    messages.success(request, "Logged out")

    return redirect("login")

class PredireAPIView(APIView):
    def post(self, *args, **kwargs):
        donnees_recues = self.request.data
        # la fonction permettant de faire une prédiction sera implémentée ou appelée ici
        # pour l'instant l'API renvoie une valeur fictive
        donnees_envoyees = {
            "prix": 2345
        }

        return Response(donnees_envoyees)
