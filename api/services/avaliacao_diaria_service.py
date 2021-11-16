from rest_framework import serializers
from ..models import AvaliacaoDiaria

def verificar_avaliacao_usuario(diaria_id, usuario_id):
    avaliacoes_diaria = AvaliacaoDiaria.objects.filter(diaria=diaria_id).filter(avaliador__isnull=False)
    for avaliacao in avaliacoes_diaria:
        if avaliacao.avaliador.id == usuario_id:
            return True
    return False

def verificar_avaliacao(diaria_id):
    avaliacoes_diaria = AvaliacaoDiaria.objects.filter(diaria=diaria_id)
    return avaliacoes_diaria.count()