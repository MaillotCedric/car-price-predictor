import os
import joblib
from django.conf import settings

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from rest_framework import serializers
from sklearn.ensemble import RandomForestRegressor

import pandas as pd

from .serializers import *


def pipeline_transformer2():
    model_path = os.path.join(settings.BASE_DIR, 'app', 'models_ai')
    pipeline_transformer = joblib.load(model_path+'/transformers/full_pipeline2.pkl')

    return pipeline_transformer

def pipeline_transformer():
    model_path = os.path.join(settings.BASE_DIR, 'app', 'models_ai')
    pipeline_transformer = joblib.load(model_path+'/transformers/full_pipeline.pkl')

    return pipeline_transformer

def validate_s(serializer):
    if serializer.is_valid():
        pass
    else:
        raise serializers.ValidationError(serializer.__str__)


def validate_r(request):
    validate_s(CarburantsListeSerializer(data=request.POST))
    validate_s(CategoriesListeSerializer(data=request.POST))
    validate_s(CouleursListeSerializer(data=request.POST))
    validate_s(IntervallesProductionListeSerializer(data=request.POST))
    validate_s(MarquesListeSerializer(data=request.POST))
    # validate_s(ModelesListeSerializer(data=request.POST))
    validate_s(OuverturesListeSerializer(data=request.POST))
    validate_s(RouesMotricesListeSerializer(data=request.POST))
    validate_s(TransmissionsListeSerializer(data=request.POST))
    # validate_s(VoituresListeSerializer(data=request.POST))

    print(request.data)
    print(request.data.get('Levy'))
    print('--------------yyyyy-----------')
    print(request.POST)
    
    levy = request.data.get('Levy')
    manufacturer = request.data.get('Manufacturer')
    model = request.data.get('Model')
    year = request.data.get('Prod. year')
    category = request.data.get('Category')
    leather_interior = request.data.get('Leather interior')
    fuel_type = request.data.get('Fuel type')
    engine_volume = request.data.get('Engine volume')
    mileage = request.data.get('Mileage')
    cylinders = request.data.get('Cylinders')
    gear_box_type = request.data.get('Gear box type')
    drive_wheels = request.data.get('Drive wheels')
    doors = request.data.get('Doors')
    wheel = request.data.get('Wheel')
    color = request.data.get('Color')
    airbags = request.data.get('Airbags')
    turbo = request.data.get('Turbo')

    # initialise data of lists.
    data = {
        'Levy':[levy],
        'Manufacturer':[manufacturer],
        'Model':[model],
        'Prod. year':[year],
        'Category':[category],
        'Leather interior':[leather_interior],
        'Fuel type':[fuel_type],
        'Engine volume':[engine_volume],
        'Mileage':[mileage],
        'Cylinders':[cylinders],
        'Gear box type':[gear_box_type],
        'Drive wheels':[drive_wheels],
        'Doors':[doors],
        'Wheel':[wheel],
        'Color':[color],
        'Airbags':[airbags],
        'Turbo':[turbo],
    }

    df = pd.DataFrame(data)

    return df
