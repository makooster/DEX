from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import RegisterView, dashboard_view, login_user,logout_user
from django.urls import path

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path('api/login/', login_user, name='login'),
    path('api/logout/', logout_user, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard')
]