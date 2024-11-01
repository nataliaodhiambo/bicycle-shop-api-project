from django.shortcuts import render
from .models import Bicycle, Product

def home(request):
    bicycles = Bicycle.objects.all()
    context = {'bicycles': bicycles}
    return render(request, 'home.html', context)

def products(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "myApp/products.html", context)