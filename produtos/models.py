from django.db import models

# Create your models here.


class Produto(models.Model):
   
    #status 
    STATUS = (('fisica', 'Fisica'),('juridica', 'Juridica'))
    
    pessoa = models.CharField(
        max_length =8,
        choices = STATUS,
    )
    

    ativo = models.BooleanField(default=True)


   #identificação
    empresa = models.CharField(max_length=255,blank=True, null=True)
    importado = models.BooleanField(blank=True, null=True)
    produto = models.CharField(max_length=100, blank=True, null=True)
    qtde = models.IntegerField(blank=True, null=True)
    valorUn = models.DecimalField('valor unitário', max_digits=7, decimal_places=2)
    estoque_minimo = models.PositiveBigIntegerField('estoque minimo', default=0,blank=True, null=True)
    estoque = models.IntegerField(blank=True, null=True)
    obs = models.TextField(blank=True, null=True)
    fornecedor = models.CharField(max_length=255,blank=True)
    os = models.CharField(max_length=8,blank=True)
    #cliente = models.CharField(max_length=255,blank=True)
    docto = models.CharField(max_length=15,blank=True, null=True)
    codigo = models.CharField(max_length=20,blank=True)
    pessoa = models.CharField(max_length=255,blank=True, null=True)

    
    
    STATUSun = (('un', 'UN'),('pc', 'PC'),('cx', 'CX'),('dz', 'DZ'),('cj', 'CJ'),('mt', 'MT'),('m2', 'M2'),('kg', 'KG'),('frd', 'FRD'))
    
    un = models.CharField(
        max_length =3,
        choices = STATUSun,
        blank=True
    )

    #impostos
    icms = models.CharField(max_length=255,blank=True)
    ipi = models.CharField(max_length=255,blank=True)
    cofins = models.CharField(max_length=255,blank=True)

    #datas
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)

    #valor
    
    lote = models.CharField(max_length=8,blank=True)
    codProd = models.CharField(max_length=20,blank=True,verbose_name='código do produto')
    qtde_tot = models.IntegerField(blank=True,null=True,)
    
    class Meta:
        ordering = ('produto',)
       

    def __str__(self):
        return self.produto
