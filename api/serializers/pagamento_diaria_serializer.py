from rest_framework import serializers

class PagamentoDiariaSerializer(serializers.Serializer):
    card_hash = serializers.CharField(required=True)