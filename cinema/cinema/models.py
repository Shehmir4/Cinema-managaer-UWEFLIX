from django.db import models


class club(models.Model):
    roll = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    phone = models.CharField(max_length=100)