from ..models import Usuario, Diaria

def listar_oportunidades(diarista_id):
    cidades_atendidas_usuario = Usuario.diarista_objects.cidades_atendidas(diarista_id)
