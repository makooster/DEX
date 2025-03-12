from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarDetailOrderViewSet

router = DefaultRouter()
router.register(r'details', CarDetailOrderViewSet)  

urlpatterns = [
    path('', include(router.urls)), 
]
