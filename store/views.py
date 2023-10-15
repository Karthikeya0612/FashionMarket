from django.shortcuts import render
from . import models

# Create your views here.
def home(request):
    dests = models.Destination.objects.all()

    return render(request, 'store/index.html', {'dests' : dests})

def beauty(request):
    return render(request, 'store/beauty.html')

def boys(request):
    return render(request, 'store/boys.html')

def girls(request):
    return render(request, 'store/girls.html')

def grooming(request):
    return render(request, 'store/grooming.html')

def infants(request):
    return render(request, 'store/infants.html')

def kurtis(request):
    return render(request, 'store/kurtis.html')

def maternity(request):
    return render(request, 'store/maternity.html')

def sandals(request):
    return render(request, 'store/sandals.html')

def sarees(request):
    return render(request, 'store/sarees.html')

def shirts(request):
    return render(request, 'store/shirts.html')

def shoes(request):
    return render(request, 'store/shoes.html')

def toys(request):
    return render(request, 'store/toys.html')

def trousers(request):
    return render(request, 'store/trousers.html')

