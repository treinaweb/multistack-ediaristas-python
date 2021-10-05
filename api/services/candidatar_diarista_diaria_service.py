import datetime
from ..models import Diaria, Usuario

def relacionar_candidata_diaria(diaria_id, diarista_id):
    diaria = Diaria.objects.get(id=diaria_id)
    if verificar_diferenca_data_contratacao(diaria.created_at) > datetime.timedelta(hours=24):
        contratar_diarista_diaria(diaria, diarista_id)


def contratar_diarista_diaria(diaria, diarista_id):
    diarista = Usuario.objects.get(id=diarista_id)
    diaria.diarista = diarista
    diarista.status = 3
    diaria.save()

def verificar_diferenca_data_contratacao(data_diaria):
    data_atual = datetime.datetime.now()
    data_diaria_criacao = data_diaria.replace(tzinfo=None)
    diferenca = data_atual - data_diaria_criacao
    return abs(diferenca)