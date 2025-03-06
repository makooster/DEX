from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Auto(models.Model):
    brand = models.CharField(max_length=50)  
    model = models.CharField(max_length=50) 
    year = models.PositiveIntegerField()  
    mileage = models.PositiveIntegerField()  # km or miles
    fuel_type = models.CharField(max_length=20, choices=[("petrol", "Petrol"), ("diesel", "Diesel"), ("electric", "Electric")])
    transmission = models.CharField(max_length=20, choices=[("manual", "Manual"), ("automatic", "Automatic")])
    body_type = models.CharField(max_length=30, choices=[("sedan", "Sedan"), ("SUV", "SUV"), ("hatchback", "Hatchback")])
    color = models.CharField(max_length=30, blank=True, null=True)
    vin_number = models.CharField(max_length=17, unique=True, blank=True, null=True) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
