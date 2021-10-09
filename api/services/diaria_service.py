from ..models import Diaria
from .usuario_service import listar_usuario_id
from .endereco_diarista_service import listar_endereco_diarista

def listar_diaria_id(diaria_id):
    return Diaria.objects.get(id=diaria_id)


def atualizar_status_diaria(diaria_id, status):
    diaria = listar_diaria_id(diaria_id)
    diaria.status = status
    diaria.save()


def listar_diarias_usuario(usuario_id):
    usuario = listar_usuario_id(usuario_id)
    if usuario.tipo_usuario == 1:
        return Diaria.objects.filter(cliente=usuario.id).all()
    return Diaria.objects.filter(diarista=usuario.id).all()


def calcular_indice_compatibilidade(diaria_id, diarista_id):
    diaria = listar_diaria_id(diaria_id)
    diarista = listar_usuario_id(diarista_id)
    reputacao_diarista = diarista.reputacao
    endereco_diarista = listar_endereco_diarista(diarista_id)
    distancia_diarista_diaria = 100 # depois implementar o método pra pegar a distancia
    return (reputacao_diarista - (distancia_diarista_diaria/10)) / 2