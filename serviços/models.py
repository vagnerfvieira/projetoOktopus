from django.db import models

# Create your models here.
class GrupoServiço(models.Model):
    nomeGrupoServ = models.CharField(max_length=25)
   
    def __str__(self):
        return self.nomeGrupoServ
    
class SubGrupoServiço(models.Model):
    
    grupoServ = models.ForeignKey('GrupoServiço', on_delete=models.CASCADE, related_name='subgrupo')
    nomeSubGrupoServ = models.CharField(max_length=25)
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
  
    def __str__(self):
        return self.nomeSubGrupoServ

    
class Serviço(models.Model):
    subGrupoServ = models.ForeignKey('SubGrupoServiço', on_delete=models.CASCADE, related_name='serviço')
    nomeServiço = models.CharField(max_length=25)
    dt_created = models.DateTimeField(auto_now_add = True)
    dt_update = models.DateTimeField(auto_now = True)
    dt_enc = models.DateTimeField(blank=True, null=True)
  

    def __str__(self):
        return self.nomeServiço
