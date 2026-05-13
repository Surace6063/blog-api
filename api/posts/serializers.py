from rest_framework import serializers
from .models import Category, Post

# category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category     # category model  
        fields = '__all__'   # select all category field


# post serializer
class PostSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    class Meta:
        model = Post     # poat model  
        fields = '__all__'   # select all post field        