from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=1000)
    age=models.IntegerField()
    email=models.EmailField(max_length=30)
    details=models.TextField(max_length=20000)
    
