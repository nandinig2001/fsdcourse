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
