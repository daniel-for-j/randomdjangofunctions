from django.db import models

# Create your models here.

class People(models.Model):
    email = models.CharField(max_length=100)
    name  = models.CharField(max_length=100)
