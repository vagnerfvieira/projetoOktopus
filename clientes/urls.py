from django.urls import path
from . import views

urlpatterns = [
    
    path('cliente/<int:id>', views.viewCliente, name='view-cliente' ),
    path('novocliente/', views.novoCliente, name='novo-cliente'),
    path('listacliente/', views.listaCliente, name='lista-cliente'),
    path('editCliente/<int:id>', views.editCliente, name='edit-cliente'),
    
]
