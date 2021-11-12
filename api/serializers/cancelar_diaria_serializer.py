from rest_framework import serializers

class CancelarDiariaSerializer(serializers.Serializer):
    motivo_cancelamento = serializers.CharField()