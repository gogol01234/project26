from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Model1(models.Model):
   
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    messages = models.TextField()
    def __str__(self):
        return self.name
class Model2(models.Model):
       
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    messages = models.TextField()
    def __str__(self):
        return self.name
