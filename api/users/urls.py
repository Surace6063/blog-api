from django.urls import path
from .views import *

urlpatterns = [
    # POST -> http://127.0.0.1:8000/api/auth/register/
    path('register/',RegisterView.as_view())
]