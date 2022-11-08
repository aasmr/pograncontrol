from django.db import models

# Create your models here.
class Pograncontrol(models.Model):
    age = models.CharField(max_length=3)
    cause = models.CharField(max_length=100)
    vus = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    kpp = models.CharField(max_length=50)
    yService = models.CharField(max_length=15)
    voenk = models.CharField(max_length=50)
    kategory = models.CharField(max_length=3)
    katZ = models.CharField(max_length=1)
    date  = models.DateField()
