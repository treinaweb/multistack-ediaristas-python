from django.urls.base import reverse
from rest_framework import serializers
from ..models import Diaria, Usuario
from ..hateoas import Hateoas

class AvaliacoesOportunidadeSerializer(serializers.BaseSerializer):
    def to_representation(self):
        return [
            {
                'descricao': 'teste',
                'nota': 5,
                'nome_avaliador': 'João',
                'foto_avaliador': 'joao.png'
            },
            {
                'descricao': 'teste',
                'nota': 5,
                'nome_avaliador': 'Maria',
                'foto_avaliador': 'joao.png'
            }
        ]

class ClienteOportunidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('nome_completo', 'telefone', 'nascimento', 'tipo_usuario', 'reputacao', 
        'foto_usuario')

class OportunidadeSerializer(serializers.ModelSerializer):
    nome_servico = serializers.SerializerMethodField()
    cliente = ClienteOportunidadeSerializer()
    links = serializers.SerializerMethodField()
    avaliacoes_cliente = serializers.SerializerMethodField()

    class Meta:
        model = Diaria
        fields = '__all__'


    def get_nome_servico(self, obj):
        return obj.servico.nome

    def get_avaliacoes_cliente(self, obj):
        return AvaliacoesOportunidadeSerializer().to_representation()

    def get_links(self, obj):
        usuario = self.context['request'].user
        links = Hateoas()
        if obj.status == 2:
            links.add_get('self', reverse('diaria-detail', kwargs={'diaria_id': obj.id}))
            candidatas = obj.candidatas.all()
            if usuario not in candidatas:
                links.add_post('candidatar_diaria', 
                reverse('candidatar-diarista-diaria-list', kwargs={'diaria_id': obj.id}))
        return links.to_array()