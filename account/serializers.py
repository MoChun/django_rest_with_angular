from rest_framework import serializers
from account.models import Record,Category

'''
class Category(models.Model):
    name=models.CharField(max_length=20)
    created_time=models.DateTimeField(auto_now_add=True)

class Record(models.Model):
    title=models.CharField(max_length=60)
    content=models.TextField()
    created_time=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
    category = models.ManyToManyField(Category)
'''


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Record
        fields=('title','author','content','category','created_time')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        models=Category
        fields=('name')