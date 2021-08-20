from django.db import models
from rest_framework import serializers
from ..models import Diaria, Usuario
from administracao.services import servico_service

class UsuarioDiariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'nascimento', 'telefone', 'tipo_usuario', 'reputacao', 
        'foto_usuario')

class DiariaSerializer(serializers.ModelSerializer):
    cliente = UsuarioDiariaSerializer(read_only=True)
    valor_comissao = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
    class Meta:
        model = Diaria
        fields = '__all__'

    def create(self, validated_data):
        servico = servico_service.listar_servico_id(validated_data["servico"].id)
        valor_comissao = validated_data["preco"] * (servico.porcentagem_comissao / 100)
        diaria = Diaria.objects.create(valor_comissao=valor_comissao,
        cliente_id=self.context['request'].user.id,
        **validated_data)
        return diaria

    def validate_preco(self, preco):
        servico = servico_service.listar_servico_id(self.initial_data["servico"])
        if servico is None:
            raise serializers.ValidationError("Serviço não existe")
        valor_total = 0
        valor_total += servico.valor_quarto * self.initial_data["quantidade_quartos"]
        valor_total += servico.valor_sala * self.initial_data["quantidade_salas"]
        valor_total += servico.valor_banheiro * self.initial_data["quantidade_banheiros"]
        valor_total += servico.valor_cozinha * self.initial_data["quantidade_cozinhas"]
        valor_total += servico.valor_quintal * self.initial_data["quantidade_quintais"]
        valor_total += servico.valor_outros * self.initial_data["quantidade_outros"]
        if preco == valor_total or preco == servico.valor_minimo:
            if valor_total >= servico.valor_minimo:
                return preco
            return servico.valor_minimo
        raise serializers.ValidationError("Valores não correspondem")

