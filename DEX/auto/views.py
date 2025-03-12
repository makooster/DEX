from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Auto
from .serializers import AutoSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Users can read, but need to be logged in to edit

# Create your views here.
