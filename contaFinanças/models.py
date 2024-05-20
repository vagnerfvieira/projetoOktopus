from django.db import models

# Create your models here.
class GrupoFinConta(models.Model):
    nomeGrupoFin = models.CharField(max_length=25)
   
    def __str__(self):
        return self.nomeGrupoFin
    
class SubGrupoFinConta(models.Model):
    
    grupoFin = models.ForeignKey('GrupoFinConta', on_delete=models.CASCADE, related_name='subgrupo')
    nomeSubGrupoFinConta = models.CharField(max_length=25)
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
  
    def __str__(self):
        return self.nomeSubGrupoFinConta

    
class ContaFin(models.Model):
    subGrupoContaFin = models.ForeignKey('SubGrupoFinConta', on_delete=models.CASCADE, related_name='conta')
    nomeContaFin = models.CharField(max_length=25)
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
  

    def __str__(self):
        return self.nomeContaFin
