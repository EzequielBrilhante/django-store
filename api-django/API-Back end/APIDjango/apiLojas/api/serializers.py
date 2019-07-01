from rest_framework import serializers
from .models import *


class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estabelecimento
        fields = ['id', 'nome', 'descricao', 'endereco']