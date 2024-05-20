from django import forms
from .models import Fornecedor

class FornecedorForm(forms.ModelForm):
    
    class Meta:
        model = Fornecedor
        fields = ('pessoa',
                  'ativo',
                  'nome',
                  'cpf',
                  'cnpj',
                  'rg',
                  'email',
                  'telCelular',
                  'telFixo',
                  'dt_enc')

