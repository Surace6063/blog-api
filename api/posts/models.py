from django.db import models

# Create your models here.

# category model
class Category(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# post model
class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField()
    author = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='posts/',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"
