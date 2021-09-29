from rest_framework import serializers

class RelacionarCidadeDiaristaSerializer(serializers.Serializer):
    cidades = serializers.ListField(required=False)