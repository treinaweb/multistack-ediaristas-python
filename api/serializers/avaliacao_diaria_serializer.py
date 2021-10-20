from rest_framework import serializers
from ..models import AvaliacaoDiaria

class AvaliacaoDiariaSerializer(serializers.ModelSerializer):
    diaria = serializers.PrimaryKeyRelatedField(read_only=True)
    avaliador = serializers.PrimaryKeyRelatedField(read_only=True)
    avaliado = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = AvaliacaoDiaria
        fields = ('descricao', 'nota', 'avaliado', 'avaliador', 'diaria')