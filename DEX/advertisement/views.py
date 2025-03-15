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
    ordering_fields = ['created_at','updated_at'] # Сортировка по времени
    ordering = ['-created_at'] # По умолчанию новые объявления первыми
    
    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)  
