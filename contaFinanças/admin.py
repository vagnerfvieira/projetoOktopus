from django.contrib import admin
from .models import GrupoFinConta
from .models import SubGrupoFinConta
from .models import ContaFin

# Register your models here.


admin.site.register(GrupoFinConta)
admin.site.register(SubGrupoFinConta)
admin.site.register(ContaFin)
