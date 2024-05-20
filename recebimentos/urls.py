from django.urls import path
from . import views

urlpatterns = [
    path('recebimento/<int:id>', views.viewRecebimento, name='view-recebimento' ),
    path('editRecebimento/<int:id>', views.editRecebimento, name='edit-recebimento'),
    path('delete/<int:id>', views.deleteRecebimento, name='delete-recebimento'),
    path('novorecebimento/', views.novoRecebimento, name='novo-recebimento'),
    path('listarecebimento/', views.listaRecebimento, name='lista-recebimento'),   
]


