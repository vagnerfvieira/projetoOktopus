from django.urls import path
from . import views

urlpatterns = [
    path('despesa/<int:id>', views.viewDespesa, name='view-despesa' ),
    path('editDespesa/<int:id>', views.editDespesa, name='edit-despesa'),
    path('delete/<int:id>', views.deleteDespesa, name='delete-despesa'),
    path('novadespesa/', views.novaDespesa, name='nova-despesa'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('listadespesa/', views.listaDespesa, name='lista-despesa'),   
]