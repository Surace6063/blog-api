from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # POST (register) -> http://127.0.0.1:8000/api/auth/register/
    path('register/',RegisterView.as_view()),
    
    # POST (login) -> http://127.0.0.1:8000/api/auth/login/
    path('login/', TokenObtainPairView.as_view()),
    
    # POST (refresh) -> http://127.0.0.1:8000/api/auth/token/refresh/
    path('token/refresh/', TokenRefreshView.as_view()),
]