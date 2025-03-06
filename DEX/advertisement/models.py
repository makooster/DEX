from django.db import models
from auto.models import Auto
from django.contrib.auth import get_user_model

User = get_user_model()

class Advertisement(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)  
    seller = models.ForeignKey(User, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    description = models.TextField(blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=20, choices=[("active", "Active"), ("sold", "Sold"), ("expired", "Expired")])
    
    def __str__(self):
        return f"Ad for {self.auto.brand} {self.auto.model} - ${self.price}"
