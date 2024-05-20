from django.urls import path
from product import views as v

urlpatterns = [
  
    path('product_list/', v.ProductListView.as_view(), name='product_list'),   
    path('create/', v.product_create, name='product_create'),
]