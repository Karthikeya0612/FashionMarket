from django.contrib import admin
from store.models import Product, Destination, ProductsOffered

# Register your models here.
admin.site.register(Product)
admin.site.register(Destination)
admin.site.register(ProductsOffered)
