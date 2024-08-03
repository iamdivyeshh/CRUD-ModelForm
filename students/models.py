from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=200)
    number = models.IntegerField()
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)