

from django.db import models

# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    description = models.CharField(max_length=1000)
    
