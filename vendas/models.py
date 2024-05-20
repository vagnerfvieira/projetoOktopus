from django.db import models
from clientes.models import Cliente
from produtos.models import Produto

# Create your models here.


class Venda(models.Model):
    
    STATUS = (('fisica', 'Fisica'),('juridica', 'Juridica'))
    
    pessoa = models.CharField(
        max_length =8,
        choices = STATUS,
    )
    ativo = models.BooleanField(default=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)    
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)  
    email = models.EmailField(max_length=255)
    telCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telFixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    empresa = models.CharField(max_length=255)
    
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)

