from django import forms
from .models import Recebimento

class RecebimentoForm(forms.ModelForm):
    
    class Meta:
        model = Recebimento
        fields = (
                    'empresa',
                    'dt_real',
                    'os',
                    'cliente',
                    'remetente',
                    'conta',
                    'valor',
                    'doctos',
                    'obs',
                    'banco'
                    )
    