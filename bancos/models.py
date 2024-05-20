from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# dinheiro = models.DecimalField(max_digits=10, decimal_plases=2)

class Banco(models.Model):    
    
    #moeda
    saldoBco = models.DecimalField(max_digits=10, decimal_places=2)
    
    #identificação    
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_real = models.DateField()
    dt_conc = models.DateField(blank=True, null=True)
    
    obs = models.TextField(blank=True, null=True)
    nome = models.CharField(max_length=255)
    agConta = models.CharField(max_length=15,blank=True, null=True)
    numerConta = models.CharField(max_length=15,blank=True, null=True)
    telBco = models.CharField(max_length=15,blank=True, null=True)
    os = models.CharField(max_length=8,blank=True)
    cliente = models.CharField(max_length=255,blank=True)
    conta = models.CharField(max_length=15,blank=True, null=True)
    doctos = models.CharField(max_length=15,blank=True, null=True)
    empresa = models.CharField(max_length=255)
    
    #status
    STATUS = (('doing', 'Doing'),('done', 'Done'))
    
    done = models.CharField(
        max_length =5,
        choices = STATUS,blank=True
    )
    
    
class DespesaBanco(models.Model):
    
    grupoFin = models.ForeignKey('GrupoFinConta', on_delete=models.CASCADE, related_name='subgrupo')
    nomeSubGrupoFinConta = models.CharField(max_length=25)
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
  
    def __str__(self):
        return self.nomeSubGrupoFinConta
    
    #moeda
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    #datas
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_real = models.DateField()
    dt_conc = models.DateField(blank=True, null=True)
    
    #identificação
    obs = models.TextField(blank=True, null=True)
    favorecido = models.CharField(max_length=255)
    os = models.CharField(max_length=8,blank=True)
    cliente = models.CharField(max_length=255,blank=True)
    conta = models.CharField(max_length=15,blank=True, null=True)
    doctos = models.CharField(max_length=15,blank=True, null=True)
    empresa = models.CharField(max_length=255)
    
    #pagamento
    banco = models.CharField(max_length=255,blank=True)
    caixa = models.CharField(max_length=255,blank=True)
    
    
    
    def __str__(self):
        return self.nome