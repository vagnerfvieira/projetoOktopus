from django.urls import path
from . import views, htmx_views

urlpatterns = [
    
    path('preçoVendas_list/', views.preçoVendas_list, name= 'preçoVendas_list'),
    path('preçoVenda_add/', views.preçoVenda_add, name='preçoVenda_add'),
    path('preçoVenda_edit/<int:id>', views.preçoVenda_edit, name='preçoVenda_edit'),
    path('preçoVenda_delete/<int:id>', views.preçoVenda_delete, name='preçoVenda_delete'),
]

htmx_urlpatterns = [
    path('preço_venda_calc/', htmx_views.preço_venda_calc, name="preço_venda_calc"),

]

urlpatterns += htmx_urlpatterns