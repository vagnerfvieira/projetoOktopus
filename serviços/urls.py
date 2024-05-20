from django.urls import path
from . import views

urlpatterns = [
    
    path('serviço/<int:id>', views.viewserviço, name='view-serviço' ),
    path('editserviço/<int:id>', views.editserviço, name='edit-serviço'),
    path('delete/<int:id>', views.deleteserviço, name='delete-serviço'),
    path('novoserviço/', views.novaserviço, name='novo-serviço'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('listaserviço/', views.listaserviço, name='lista-serviço'), 
    
    path('gruposerviço/<int:id>', views.viewgruposerviço, name='view-gruposerviço' ),
    path('editgruposerviço/<int:id>', views.editgruposerviço, name='edit-gruposerviço'),
    path('delete/<int:id>', views.deletegruposerviço, name='delete-gruposerviço'),
    path('novogruposerviço/', views.novogruposerviço, name='nova-gruposerviço'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('listagruposerviço/', views.listagruposerviço, name='lista-gruposerviço'), 
    
    path('subgruposerviço/<int:id>', views.viewsubgruposerviço, name='view-subgruposerviço' ),
    path('editsubgruposerviço/<int:id>', views.editsubgruposerviço, name='edit-subgruposerviço'),
    path('delete/<int:id>', views.deletesubgruposerviço, name='delete-subgruposerviço'),
    path('novosubgruposerviço/', views.novosubgruposerviço, name='nova-subgruposerviço'),
    path('changestatus/<int:id>', views.changeStatus, name='change-status'),
    path('listasubgruposerviço/', views.listasubgruposerviço, name='lista-subgruposerviço'),   
]