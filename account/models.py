from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)
    created_time=models.DateTimeField(auto_now_add=True)

class Record(models.Model):
    title=models.CharField(max_length=60)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
    category = models.ManyToManyField(Category)










