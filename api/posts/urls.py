from django.urls import path
from .views import *

urlpatterns = [
    # GET and POST -> http://127.0.0.1:8000/api/categories/
    path('categories/',CategoryListCreateView.as_view()),
    
    # GET(single), PATCH and DELETE -> http://127.0.0.1:8000/api/categories/pk/
    # pk -> id of category like 1,2,3...
    path('categories/<int:pk>/',CategoryRetriveUpdateDistroyView.as_view()),
    
    
    # GET and POST -> http://127.0.0.1:8000/api/posts/
    path('posts/',PostListCreateView.as_view()),
    
    # GET(single), PATCH and DELETE -> http://127.0.0.1:8000/api/posts/pk/
    # pk -> id of post like 1,2,3...
    path('posts/<int:pk>/',PostRetriveUpdateDistroyView.as_view()),
]