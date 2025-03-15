from rest_framework import viewsets, permissions
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [permissions.IsAuthenticated]  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'price',
        'status',
        'auto__brand',         
        'auto__model',         
        'auto__year',
        ]
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)  
