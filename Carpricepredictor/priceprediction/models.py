from django.db import models
# Create your models here.

class Car(models.Model):
    car_name=models.CharField(max_length=30)
    year=models.IntegerField()
    km_driven=models.FloatField()
    fuel_type=models.IntegerField()
    seller_type=models.IntegerField()
    transmission=models.IntegerField()
