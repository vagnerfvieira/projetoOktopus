from django.db import models

# Create your models here.


class Empresa(models.Model):
      
    ativo = models.BooleanField(default=True)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True,blank=True)
    email = models.EmailField(max_length=255,blank=True)
    telCelular = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telFixo = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')

    
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
    
    cep = models.CharField(max_length=10,blank=True)
    bairro = models.CharField(max_length=255,blank=True)
    rua = models.CharField(max_length=255,blank=True)
    complemento = models.CharField(max_length=255,blank=True)
    numero = models.CharField(max_length=10,blank=True)
    estado = models.CharField(max_length=2,blank=True)
    cidade = models.CharField(max_length=255,blank=True)
    
    cep2 = models.CharField(max_length=10,blank=True)
    bairro2 = models.CharField(max_length=255,blank=True)
    rua2 = models.CharField(max_length=255,blank=True)
    complemento2 = models.CharField(max_length=255,blank=True)
    numero2 = models.CharField(max_length=10,blank=True)
    estado2 = models.CharField(max_length=2,blank=True)
    cidade2 = models.CharField(max_length=255,blank=True)
    email2 = models.EmailField(max_length=255,blank=True)
    telCelular2 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone celular')
    telFixo2 = models.CharField(max_length=11, blank=True, null=True, verbose_name='Nº telefone fixo')    
    
    def __str__(self):
        return self.nome