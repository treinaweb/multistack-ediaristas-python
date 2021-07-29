from rest_framework import serializers
from administracao.models import Servico

class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'