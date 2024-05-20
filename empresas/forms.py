from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    
    class Meta:
        model = Empresa
        fields = (
                    'ativo',
                    'nome',
                    'cnpj',
                    'rua',
                    'numero',
                    'bairro',
                    'complemento',
                    'cep',
                    'cidade',
                    'estado',
                    'email',
                    'telCelular',
                    'telFixo',
                    'rua2',
                    'numero2',
                    'bairro2',
                    'complemento2',
                    'cep2',
                    'cidade2',
                    'estado2',
                    'email2',
                    'telCelular2',
                    'telFixo2',
                    )
    