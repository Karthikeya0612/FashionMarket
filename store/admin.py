from django.contrib import admin
from store.models import Destination, ProductsOffered, Carousel, Cart, CartItem
# Register your models here.
admin.site.register(Destination)
admin.site.register(ProductsOffered)
admin.site.register(Carousel)
admin.site.register(CartItem)
admin.site.register(Cart)

