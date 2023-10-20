from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    id = models.AutoField(primary_key=True, editable=False)
    img = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
    
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