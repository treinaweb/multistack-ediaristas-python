from ..models import EnderecoDiarista

def listar_endereco_diarista(diarista_id):
    return EnderecoDiarista.objects.get(usuario=diarista_id)