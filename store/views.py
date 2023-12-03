from django.shortcuts import render, redirect
from . import models
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login')
def add_to_cart(request, product_id):
    product = models.ProductsOffered.objects.get(pk=product_id)
    cart, created = models.Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = models.CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('..')

@login_required(login_url='login')
def remove_from_cart(request, product_id):
    product = models.ProductsOffered.objects.get(pk=product_id)
    cart = models.Cart.objects.get(user=request.user)
    try:
        cart_item = cart.cartitem_set.get(product=product)
        if cart_item.quantity >= 1:
             cart_item.delete()
    except models.CartItem.DoesNotExist:
        pass
    
    return redirect('cart')

@login_required(login_url='login')
def view_cart(request):
    cart = request.user.cart
    cart_items = models.CartItem.objects.filter(cart=cart)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

