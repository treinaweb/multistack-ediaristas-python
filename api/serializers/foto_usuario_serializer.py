from rest_framework import serializers

class FotoUsuarioSerailizer(serializers.Serializer):
    foto_usuario = serializers.ImageField()