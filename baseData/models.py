from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length = 50)
    fono = models.CharField(max_length=15)