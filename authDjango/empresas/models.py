import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Empresa(models.Model):
    guid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    simbolo = models.CharField(max_length=10)
    valores_mercado = ArrayField(models.CharField(max_length=50))
    '''
    def __init__(self, name, description, simbolo):
        self.name = name
        self.description = description
        self.simbolo = simbolo
    '''

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'empresas'
