from django import forms
from .models import Venda

class VendaForm(forms.ModelForm):
    
    class Meta:
        model = Venda
        fields = (
                'empresa',
                'pessoa',
                'ativo',
                'nome',
                'cpf',
                'cnpj',
                'rg',
                'email',
                'telCelular',
                'telFixo',
                'dt_enc'
                )

