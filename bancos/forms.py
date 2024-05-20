from django import forms
from .models import Despesa

class DespesaForm(forms.ModelForm):
    
    class Meta:
        model = Despesa
        fields = (
                    'empresa',
                    'dt_real',
                    'os',
                    'cliente',
                    'favorecido',
                    'conta',
                    'valor',
                    'doctos',
                    'obs',
                    'banco'
                    )
    