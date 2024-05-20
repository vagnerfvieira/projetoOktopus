from django.urls import path
from . import views

urlpatterns = [
    
    path('estoque_entrada_list/', views.entrada_estoque_list, name='entrada_estoque_list'),
    path('estoque_entrada_detail/<int:id>', views.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('estoque_entrada_add/', views.estoque_entrada_add, name='estoque_entrada_add'),
]


