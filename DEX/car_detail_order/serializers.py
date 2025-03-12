from rest_framework import serializers
from .models import CarDetailOrder

class CarDetailOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetailOrder
        fields = "__all__"
        read_only_fields = ['request_date', 'status', 'response_data']