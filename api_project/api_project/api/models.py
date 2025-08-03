from django.db import models

# Create your models here.
class Book(models.Model):
    title= models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)