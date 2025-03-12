from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import LoginUserForm
from django.http import HttpResponse

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  
    serializer_class = RegisterSerializer

# def login_landing(request):
#     return render(request, 'login.html') 

def login_user(request):
    form = LoginUserForm()
    return render(request,'login.html',{'form':form})

def logout_user(request):
    return HttpResponse("logout")

@api_view(["GET"])
@permission_classes([IsAuthenticated])  # Ensures only logged-in users can access
def dashboard_view(request):
    return Response({"message": "Welcome to your dashboard!", "user": request.user.username})

