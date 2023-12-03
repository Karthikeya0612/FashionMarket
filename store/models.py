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

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(ProductsOffered, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(ProductsOffered, through='CartItem')

    def __str__(self):
        return f"Cart for {self.user.username}"

User.profile = property(lambda u: User.objects.get_or_create(user=u)[0])
User.cart = property(lambda u: Cart.objects.get_or_create(user=u)[0])