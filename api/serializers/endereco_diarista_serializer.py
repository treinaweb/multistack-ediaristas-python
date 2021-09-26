from rest_framework import serializers
from ..models import EnderecoDiarista

class EnderecoDiaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoDiarista
        exclude = ['usuario', ]