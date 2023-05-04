from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



import pickle
from .functions import pipeline_transformer, validate_r

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

def predict(request):
    
    data = validate_r(request)
    pipeline = pipeline_transformer()

    predictions = clf2.predict(pipeline.transform(data))

    # load model
    with open('ai-models/model.pkl', 'rb') as f:
        clf2 = pickle.load(f)
    

