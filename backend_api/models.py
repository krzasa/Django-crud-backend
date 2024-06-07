from django.db import models

# Create your models here.
class Wood(models.Model):
    cuts = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=32)
    image_url = models.URLField(max_length=200, blank=True) 

class Lighting(models.Model):
    model = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=32)
    image_url = models.URLField(max_length=200, blank=True) 

class Appliances(models.Model):
    model = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    material = models.CharField(max_length=32)
    image_url = models.URLField(max_length=200, blank=True) 

class Paint(models.Model):
    brand = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=32)
    image_url = models.URLField(max_length=200, blank=True) 

class Landscaping(models.Model):
    item = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=32)
    image_url = models.URLField(max_length=200, blank=True) 