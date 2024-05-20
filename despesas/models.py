from django.db import models
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User

from fornecedores.models import Fornecedor


# Create your models here.
# dinheiro = models.DecimalField(max_digits=10, decimal_plases=2)

class Despesa(models.Model):    
    
    #moeda
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    #datas
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_real = models.DateField()
    dt_conc = models.DateField(blank=True, null=True)
    
    #identificação
    user = models.ForeignKey(get_user_model(),on_delete=models.RESTRICT)
    obs = models.TextField(blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)    
    os = models.CharField(max_length=8,blank=True)
    cliente = models.CharField(max_length=255,blank=True)
    conta = models.CharField(max_length=15,blank=True, null=True)
    doctos = models.CharField(max_length=15,blank=True, null=True)
    empresa = models.CharField(max_length=255)
    
    #pagamento
    banco = models.CharField(max_length=255,blank=True)
    caixa = models.CharField(max_length=255,blank=True)
    
    #status
    STATUS = (('doing', 'Doing'),('done', 'Done'))
    
    done = models.CharField(
        max_length =5,
        choices = STATUS,blank=True
    )
    
    STATUSconc = (('doing', 'Doing'),('done', 'Done'))
    
    concialiado = models.CharField(
        max_length =5,
        choices = STATUS,blank=True
    )
    
    
    
    
    
def __str__(self):
        return self.banco