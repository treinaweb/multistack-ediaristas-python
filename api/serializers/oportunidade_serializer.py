from rest_framework import serializers
from ..models import Diaria, Usuario


class ClienteOportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'telefone', 'nascimento', 'tipo_usuario', 'reputacao', 
        'foto_usuario')

class OportunidadeSerializer(serializers.ModelSerializer):
    nome_servico = serializers.SerializerMethodField()
    cliente = ClienteOportunidadeSerializer()
    class Meta:
        model = Diaria
        fields = '__all__'


    def get_nome_servico(self, obj):
        return obj.servico.nome