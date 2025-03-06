from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)  
    is_broker = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
