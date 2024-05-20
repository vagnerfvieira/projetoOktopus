import uuid

from django.contrib.auth.models import User
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.




class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        'criando em',
        auto_now_add=True,
        auto_now=False
        )
    
    modified = models.DateTimeField(
        'modificado em',
        auto_now_add=False,
        auto_now=True
          )
class Meta:
    abstract = True