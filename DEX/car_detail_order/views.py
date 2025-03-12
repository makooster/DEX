from rest_framework import viewsets, permissions
from .models import CarDetailOrder
from .serializers import CarDetailOrderSerializer

class CarDetailOrderViewSet(viewsets.ModelViewSet):
    queryset = CarDetailOrder.objects.all().order_by('-request_date')
    serializer_class = CarDetailOrderSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def perform_create(self, serializer):
        serializer.save(requester=self.request.user)  
