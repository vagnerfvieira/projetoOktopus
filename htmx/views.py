from django.shortcuts import render
from . models import Product

# Create your views here.

def list_products(request):
    products = Product.objects.all()
    return render(request, 'products/list_product.html',{'products':products})





