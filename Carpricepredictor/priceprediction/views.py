from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd

def index(request):
    return render(request, 'index.html')

def getdetails(request):
    car_name = request.POST['name']
    fuel_type = request.POST['fuel']
    seller_type = request.POST['seller']
    transmission = request.POST['transmission']
    owner = request.POST['owner']
    year = request.POST['Year']
    km_driven = request.POST['km']
    present_price = 0

    model = pickle.load(open('priceprediction/model.pkl', 'rb'))
    input_variables = pd.DataFrame([[year, present_price, km_driven, fuel_type, seller_type, transmission, owner]],
                                    columns=['Year', 'Present_Price',  'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'],
                                    dtype=float)
    
    input_variables.pop('Present_Price')

    prediction = model.predict(input_variables)[0]
    return render(request, 'index.html', {'car_name':car_name,'prediction': prediction})
