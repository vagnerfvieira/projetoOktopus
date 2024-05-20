from django.urls import path
from . import views, htmx_views

urlpatterns = [
    path('produto/<int:id>', views.viewProduto, name='view-produto' ),
    path('novoproduto/', views.novoProduto, name='novo-produto'),
    path('listaproduto/', views.listaProduto, name='lista-produto'),  
    path('editproduto/<int:id>', views.editProduto, name='edit-produto'),
    path('importadordados_produto/', views.importarDadosProdutos.as_view(), name='importar_Dados'),
   
]
