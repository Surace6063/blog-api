from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from .pagination import CustomPagination


# GET and POST request
# ListCreateAPIView  -> use for both getting all categories and create new category
class CategoryListCreateView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    pagination_class = CustomPagination
    

# RetrieveUpdateDestroyAPIView -> GET(single data), PATCH/PUT and DELETE request
# Retrive -> use to get single category, Update -> update category and 
# Destroy -> delete category 
class CategoryRetriveUpdateDistroyView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




# GET and POST request
# ListCreateAPIView  -> use for both getting all posts and create new post
class PostListCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_fields = ['category__name','author','is_published']
    search_fields = ['title','description']
    ordering_fields = ['created_at','title']
    
    pagination_class = CustomPagination
    

# RetrieveUpdateDestroyAPIView -> GET(single data), PATCH/PUT and DELETE request
# Retrive -> use to get single category, Update -> update post and 
# Destroy -> delete post
class PostRetriveUpdateDistroyView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer





