from django.db import models
from django.contrib.auth import get_user_model
from auto.models import Auto
User = get_user_model()

# Create your models here.
class CarDetailOrder(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requests")
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name="details_requests")
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    comment = models.TextField(blank=True, null=True)  
    response_data = models.JSONField(blank=True, null=True)  

    def __str__(self):
        return f"Request {self.id} for {self.auto.brand} {self.auto.model} ({self.auto.year})"
