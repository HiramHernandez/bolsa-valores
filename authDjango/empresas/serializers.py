from rest_framework import serializers
from .models import Empresa


class SerializerEmpresa(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ('guid', 'name', 'description', 'simbolo', 'valores_mercado')