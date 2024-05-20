from django.contrib.auth.models import User
from core.models import TimeStampedModel
from produtos.models import Produto
from django.db import models
# Create your models here.



class PreçoVenda(TimeStampedModel):
    funcionario =   models.ForeignKey(User, on_delete=models.CASCADE)
    descricao =     models.CharField(max_length=255)
    

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.descricao, self.created.strftime('%d-%m-%Y'))
    

class PreçoVendaIten(models.Model):
    preçoVenda =        models.ForeignKey(PreçoVenda, on_delete=models.CASCADE,related_name='preçoVenda')
    produto  =          models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade =        models.PositiveIntegerField()
    #valorUn =           models.PositiveIntegerField(blank=True, null=True)
    valorUnit =         models.PositiveIntegerField(blank=True, null=True)
    descontos =         models.PositiveIntegerField(blank=True, null=True)
    percentual_imposto =       models.PositiveIntegerField(blank=True, null=True)
    valor_imposto  =      models.FloatField(blank=True, null=True) 
    fretes =            models.FloatField(blank=True, null=True)
    seguros =           models.PositiveIntegerField(blank=True, null=True)
    subsTrib =          models.PositiveIntegerField(blank=True, null=True)
    outrosCustos =      models.PositiveIntegerField(blank=True, null=True)
    custoTotal =        models.FloatField(blank=True, null=True)
    preçoVendaTotal =   models.FloatField(blank=True, null=True)
    class Meta:
        ordering = ('pk',)
    
    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.preçoVenda, self.produto)