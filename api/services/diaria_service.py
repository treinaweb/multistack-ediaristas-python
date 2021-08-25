from ..models import Diaria

def listar_diaria_id(diaria_id):
    return Diaria.objects.get(id=diaria_id)