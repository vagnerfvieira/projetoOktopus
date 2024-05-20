from django import forms
from .models import PreçoVenda, PreçoVendaIten

class PreçoVendaForm(forms.ModelForm):  
    class Meta:
        model = PreçoVenda
        fields = ('__all__')
        
class PreçoVendaItenForm(forms.ModelForm):  
    class Meta:
        model = PreçoVendaIten
        fields = ('__all__')
    