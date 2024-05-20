from django.contrib import admin
from .models import PreçoVenda, PreçoVendaIten

# Register your models here.



class PreçoVendasItensInLine(admin.TabularInline):
    model = PreçoVendaIten
    extra = 0
    
@admin.register(PreçoVenda)   
class PreçoVendasAdmin(admin.ModelAdmin):
    inlines = (PreçoVendasItensInLine,)
    list_display = ('__str__',)
    
    search_fields = ('funcioario',)
    list_filter = ('funcionario',)
    date_hierarchy = ('created')