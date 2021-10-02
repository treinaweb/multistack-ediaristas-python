from rest_framework import serializers
from ..models import Diaria, Usuario


class OportunidadeSerializer(serializers.ModelSerializer):
    nome_servico = serializers.SerializerMethodField()
    class Meta:
        model = Diaria
        fields = '__all__'


    def get_nome_servico(self, obj):
        return obj.servico.nome