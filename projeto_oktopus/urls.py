
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('despesas.urls')),
    path('', include('produtos.urls')),
    path('', include('clientes.urls')),
    path('', include('fornecedores.urls')),
    path('', include('contaFinanças.urls')),
    path('', include('empresas.urls')),
    path('', include('recebimentos.urls')),
    path('', include('estoques.urls')),
    path('', include('preçoVendas.urls')),
    path('', include('htmx.urls')),
    path('', include('calculadora.urls')),
    path('', include('product.urls')),
    path('', include('ecommerce.urls')),
   
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

#o django obedece a sequencia de urls de cima para baixo