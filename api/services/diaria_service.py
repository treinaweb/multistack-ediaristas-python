from ..models import Diaria
from .usuario_service import listar_usuario_id

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