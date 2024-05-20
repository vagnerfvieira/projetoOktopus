from django.contrib import admin
from .models import GrupoServiço
from .models import SubGrupoServiço
from .models import Serviço

# Register your models here.


admin.site.register(GrupoServiço)
admin.site.register(SubGrupoServiço)
admin.site.register(Serviço)
