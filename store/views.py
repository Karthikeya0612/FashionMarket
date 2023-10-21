from django.shortcuts import render, redirect
from . import models

results=models.ProductsOffered.objects
categories_list = results.values_list('category', flat=True).distinct()
carousels = models.Carousel.objects

def home(request):
    dests = models.Destination.objects.all()
    carousels_data = carousels.filter(label="home")
    return render(request, 'store/index.html', {'dests' : dests, 'carousels_data': carousels_data})


def show_category(request, category):
    if category in categories_list:
        data = results.filter(category=category)
        product = data.first()
        if product:
            label = product.label
        else:
            label = None
        carousels_data = list(carousels.filter(label=label))
        context = {'category_data': data, 'category_name': category.capitalize(), 'label_name': label.capitalize(), 'carousels_data': carousels_data}

    else:
        return redirect("..")

    return render(request, 'store/categories.html', context)

