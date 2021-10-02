from ..models import Usuario, Diaria

def listar_oportunidades(diarista_id):
    cidades_atendidas_usuario = Usuario.diarista_objects.cidades_atendidas(diarista_id)
    oportunidades_cidade = Diaria.diaria_objects.oportunidades_cidade(
        cidades_atendidas_usuario).filter(numero_diaristas__lt=3).exclude(
            candidatas=diarista_id)
    return oportunidades_cidade
