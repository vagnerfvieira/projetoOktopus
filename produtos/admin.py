from django.contrib import admin
from .models import Produto
# Register your models here.


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'importado',
        'estoque',
        'estoque_minimo',
        
    )
    
    search_fields=('produto', )
    list_filter = ('produto', )
    