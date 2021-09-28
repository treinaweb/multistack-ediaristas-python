from django.db import models
from rest_framework import serializers
from ..models import CidadesAtendimento

class CidadesAtendimentoDiaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CidadesAtendimento
        fields = '__all__'