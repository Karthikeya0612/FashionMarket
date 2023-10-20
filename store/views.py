from django.shortcuts import render, redirect
from . import models

results=models.ProductsOffered.objects
categories_list = models.ProductsOffered.objects.values_list('category', flat=True).distinct()

def home(request):
    dests = models.Destination.objects.all()
    return render(request, 'store/index.html', {'dests' : dests})


def show_category(request, category):
    if category in categories_list:
        data = results.filter(category=category)
        product = data.first()
        if product:
            label = product.label
        else:
            label = None

        context = {'category_data': data, 'category_name': category.capitalize(), 'label_name': label.capitalize()}

    else:
        return redirect("..")

    return render(request, 'store/categories.html', context)

