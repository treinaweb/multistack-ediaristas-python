from rest_framework import serializers

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