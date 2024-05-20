from django import forms
from .models import Serviço


class DespesaForm(forms.ModelForm):
    
    class Meta:
        model = Serviço,
        fields = (
                    'subGrupoServ',
                    'nomeServiço',
                    )
    