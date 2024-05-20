from django.urls import path
from . import views

urlpatterns = [
    path('venda/<int:id>', views.viewvenda, name='view-venda' ),
    path('editvenda/<int:id>', views.editvenda, name='edit-venda'),
    path('delete/<int:id>', views.deletevenda, name='delete-venda'),
    path('novavenda/', views.novavenda, name='nova-venda'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('listavenda/', views.listavenda, name='lista-venda'),   
]