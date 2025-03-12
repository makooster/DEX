from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AutoViewSet

router = DefaultRouter()
router.register(r'autos', AutoViewSet)  

urlpatterns = [
    path('', include(router.urls)), 
]
