from rest_framework import serializers
from ..models import EnderecoDiarista

class EnderecoDiaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoDiarista
        exclude = ['usuario', ]

    def create(self, validated_data):
        usuario = self.context['request'].user
        endereco_diarista = EnderecoDiarista.objects.update_or_create(
         usuario=usuario, defaults=validated_data
        )
        return endereco_diarista