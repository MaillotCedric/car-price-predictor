from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from category_encoders import TargetEncoder
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from rest_framework import serializers

from .serializers import *

def pipeline_transformer():
    # Features for target encoding
    car_cat1 = ["Manufacturer", "Model", "Category", "Color"]
    # Features for one hot encoding
    car_cat2 = ["Fuel type", "Gear box type", "Drive wheels", "Wheel"]

    #Initialize pipeline
    num_pipeline = Pipeline([
        ("imputer", SimpleImputer(strategy='median')),
        ("std_scalar", StandardScaler())
    ])

    #full pipeline
    pipeline_transformer = ColumnTransformer([
        ("target_encoder", TargetEncoder(), car_cat1),
        ('num', num_pipeline, ['Levy', 'Prod. year', 'Leather interior', 'Engine volume', 'Mileage', 'Cylinders', 'Doors', 'Airbags', 'Turbo']),
        ("one_hot_encoder", OneHotEncoder(), car_cat2)
    ])

    return pipeline_transformer

def validate_s(serializer):
    if serializer.is_valid():
        pass
    else:
        raise serializers.ValidationError(serializer.__str__)

def validate_r(request):
    levy = request.POST.get('levy')
    manufacturer = request.POST.get('nom')
    model = request.POST.get('model')
    year = request.POST.get('year')
    category = request.POST.get('category')
    leather_interior = request.POST.get('leather_interior')
    fuel_type = request.POST.get('fuel_type')
    engine_volume = request.POST.get('engine_volume')
    mileage = request.POST.get('mileage')
    cylinders = request.POST.get('cylinders')
    gear_box_type = request.POST.get('gear_box_type')
    drive_wheels = request.POST.get('drive_wheels')
    doors = request.POST.get('doors')
    wheel = request.POST.get('wheel')
    color = request.POST.get('color')
    airbags = request.POST.get('airbags')
    turbo = request.POST.get('turbo')

    validate_s(CarburantsListeSerializer(data=request.data))
    validate_s(CategoriesListeSerializer(data=request.data))
    validate_s(CouleursListeSerializer(data=request.data))
    validate_s(IntervallesProductionListeSerializer(data=request.data))
    validate_s(MarquesListeSerializer(data=request.data))
    validate_s(ModelesListeSerializer(data=request.data))
    validate_s(OuverturesListeSerializer(data=request.data))
    validate_s(RouesMotricesListeSerializer(data=request.data))
    validate_s(TransmissionsListeSerializer(data=request.data))
    validate_s(VoituresListeSerializer(data=request.data))

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

    																
    
    # Create DataFrame
    df = pd.DataFrame(data)

    return data
    
    
