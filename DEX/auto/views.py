from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Auto
from .serializers import AutoSerializer
from django_filters.rest_framework import DjangoFilterBackend

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Users can read, but need to be logged in to edit
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['brand','model','year']
# Create your views here.
