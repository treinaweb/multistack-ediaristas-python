from django.db import models
from rest_framework import serializers
from ..models import Diaria, Usuario

class UsuarioDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'nascimento', 'telefone', 'tipo_usuario', 'reputacao', 
        'foto_usuario')

class DiariaSerializer(serializers.ModelSerializer):
    cliente = UsuarioDiariaSerializer(read_only=True)
    class Meta:
        model = Diaria
        fields = '__all__'

    def create(self, validated_data):
        diaria = Diaria.objects.create(cliente_id=self.context['request'].user.id,
        **validated_data)
        return diaria