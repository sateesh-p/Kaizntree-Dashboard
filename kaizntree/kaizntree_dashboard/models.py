from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Item(models.Model):
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    tags = models.ManyToManyField('Tag')
    stock_status = models.CharField(max_length=20)
    in_stock =  models.DecimalField(max_digits=10, decimal_places=3)
    available_stock = models.DecimalField(max_digits=10, decimal_places=3)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.task
    
# models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
