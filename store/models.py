from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

    
class Destination(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    stock = models.IntegerField()
    img = models.ImageField(upload_to='media/')
    

class ProductsOffered(models.Model):
    name = models.CharField(max_length=100)
    label = models.CharField(max_length=10)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    st = models.IntegerField()
    img = models.ImageField(upload_to='media/')

class Carousel(models.Model):
    label = models.CharField(max_length=10)
    img = img = models.ImageField(upload_to='media/')