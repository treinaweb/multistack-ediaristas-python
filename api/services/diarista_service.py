from ..models import AvaliacaoDiaria
from ..services import usuario_service

def penalizar_diarista(diarista, diaria):
    AvaliacaoDiaria.objects.create(descricao="", nota=0, visibilidade=0, diaria=diaria,
    avaliador=None, avaliado=diarista)
    reputacao = AvaliacaoDiaria.avaliacao_objects.reputacao_usuario(diarista.id)
    usuario_service.atualizar_reputacao_usuario(diarista, reputacao['nota__avg'])