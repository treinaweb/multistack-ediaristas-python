from ..models import Diaria

def listar_diaria_id(diaria_id):
    return Diaria.objects.get(id=diaria_id)


def atualizar_status_diaria(diaria_id, status):
    diaria = listar_diaria_id(diaria_id)
    diaria.status = status
    diaria.save()