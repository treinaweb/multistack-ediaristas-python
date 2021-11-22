from datetime import date

from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from ..models import Usuario
from ..services import usuario_service

class EditarUsuarioSerializer(serializers.ModelSerializer):
    foto_usuario = serializers.ImageField(max_length=None, use_url=True, allow_null=True,
    required=False)
    password = serializers.CharField(required=False, write_only=True)
    password_confirmation = serializers.CharField(required=False, write_only=True)
    new_password = serializers.CharField(required=False, write_only=True)
    chave_pix = serializers.CharField(required=False)
    
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'cpf', 'nascimento', 'foto_usuario', 'telefone',
        'password', 'password_confirmation', 'new_password', 'chave_pix')

    def validate_new_password(self, new_password):
        password_confirmation = self.initial_data["password_confirmation"]
        if new_password != password_confirmation:
            raise serializers.ValidationError("Senhas não combinam")
        return make_password(new_password)

    def validate_password(self, password):
        usuario = self.context['request'].user
        if not usuario.check_password(password):
            raise serializers.ValidationError("A senha atual é diferente da informada")
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