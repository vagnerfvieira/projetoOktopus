from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    
    STATUS = (('fisica', 'Fisica'),('juridica', 'Juridica'))
    
    pessoa = models.CharField(
        max_length =8,
        choices = STATUS,
    )
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    rg = models.CharField(max_length=14, unique = True)
    email = models.EmailField(max_length=255)
    telCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telFixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')
    
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.nome