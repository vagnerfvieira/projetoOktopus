from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
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

