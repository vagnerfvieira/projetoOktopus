from django.urls import path
from . import views

urlpatterns = [

    path('empresa/<int:id>', views.viewEmpresa, name='view-empresa' ),
    path('novaempresa/', views.novaEmpresa, name='nova-empresa'),
    path('listaempresa/', views.listaEmpresa, name='lista-empresa'),
    path('editEmpresa/<int:id>', views.editEmpresa, name='edit-empresa'),
    path('deleteEmpresa/<int:id>', views.deleteEmpresa, name='delete-empresa'),   
]


