from django.http import HttpResponse
from . models import Produto
from django.shortcuts import render


def check_product(request):
    product = request.GET.get('product')
    products = Produto.objects.filter(produto=product)
    return render(request,'htmx_components/check_product.html',{'products':products})
    
def save_product(request):
    produto = request.POST.get('produto')
    valorUn = request.POST.get('valorUn')

    product = Produto(
        produto = produto,
        valorUn = valorUn,
    )

    product.save()