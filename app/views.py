import os
import pickle
import joblib

from rest_framework.decorators import api_view
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings

from .functions import pipeline_transformer, validate_r, pipeline_transformer2

from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response


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
# @csrf_exempt
class PredireAPIView(APIView):
    def post(self, *args, **kwargs):
        model_path = os.path.join(settings.BASE_DIR, 'app', 'models_ai')
        print(model_path)

        num_model = self.request.data.get('num_model')
        

        if num_model == 2:
            # with open(model_path+'/model.pkl', 'rb') as f:
            #     model = pickle.load(f)
            model = joblib.load(model_path+'/final_model.pkl')
            df = validate_r(self.request)
            pipeline = pipeline_transformer2()
        else:
            model = joblib.load(model_path+'/model.pkl')
            df = validate_r(self.request)
            pipeline = pipeline_transformer()


        predictions = model.predict(pipeline.transform(df))
        return Response({'result': predictions})
