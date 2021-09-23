from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Assignment(models.Model):
    name = models.CharField(max_length=100)
    g1 = models.CharField(max_length=100)
    w1= models.CharField(max_length=100)
    g2 = models.CharField(max_length=100)
    w2 = models.CharField(max_length=100)


    def __str__(self):
        return self.name
class Page(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pfname=models.CharField(max_length=200)
    plname=models.CharField(max_length=200)
    pcollege=models.CharField(max_length=200)
    pmobile=models.IntegerField()
    page=models.IntegerField()
