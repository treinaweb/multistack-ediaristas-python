from datetime import date

from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from ..models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    chave_pix = serializers.CharField(required=False)
    password_confirmation = serializers.CharField(write_only=True, required=True)
    tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
    foto_usuario = serializers.ImageField(max_length=None, use_url=True, allow_null=True,
    required=False)
    password = serializers.CharField(write_only=True)
    foto_documento = serializers.ImageField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = (
            'nome_completo',
            'cpf',
            'nascimento',
            'foto_documento',
            'telefone',
            'tipo_usuario',
            'password',
            'password_confirmation',
            'email',
            'chave_pix',
            'foto_usuario'
        )


    def validate_password(self, password):
        password_confirmation = self.initial_data["password_confirmation"]
        if password != password_confirmation:
            raise serializers.ValidationError("Senhas não combinam")
        return password


    def validate_nascimento(self, nascimento):
        data_atual = date.today()
        idade = data_atual.year - nascimento.year - (
            (data_atual.month, data_atual.day) < (nascimento.month, nascimento.day)
        )
        if idade < 18:
            raise serializers.ValidationError("Usuário menor de idade")
        if idade > 100:
            raise serializers.ValidationError("Idade maior que a permitida")
        return nascimento


    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password')
        )
        validated_data.pop('password_confirmation', None)
        usuario = Usuario.objects.create(**validated_data)
        return usuario