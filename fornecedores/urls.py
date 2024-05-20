from django.urls import path
from . import views

urlpatterns = [
    
    path('fornecedor/<int:id>', views.viewFornecedor, name='view-fornecedor' ),
    path('novofornecedor/', views.novoFornecedor, name='novo-fornecedor'),
    path('listafornecedor/', views.listaFornecedor, name='lista-fornecedor'),
    path('editfornecedor/<int:id>', views.editFornecedor, name='edit-fornecedor'),
    
]
