from django.db import models


class Recebimento(models.Model):    
    
    #moeda
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    #datas
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_real = models.DateField()
    dt_conc = models.DateField(blank=True, null=True)
    
    #identificação
    obs = models.TextField(blank=True, null=True)
    remetente = models.CharField(max_length=255)
    os = models.CharField(max_length=8,blank=True)
    cliente = models.CharField(max_length=255,blank=True)
    conta = models.CharField(max_length=15,blank=True, null=True)
    doctos = models.CharField(max_length=15,blank=True, null=True)
    empresa = models.CharField(max_length=255)
    
    
    #recebimento
    banco = models.CharField(max_length=255,blank=True)
    caixa = models.CharField(max_length=255,blank=True)
    
    #status
    STATUS = (('doing', 'Doing'),('done', 'Done'))
    
    done = models.CharField(
        max_length =5,
        choices = STATUS,blank=True
    )
    
    
    def __str__(self):
        return self.remetente