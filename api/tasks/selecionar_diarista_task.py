import datetime

from ..models import Diaria
from ..services.candidatar_diarista_diaria_service import verificar_diferenca_data_contratacao
from ..services.selecionar_diarista_service import selecionar_diarista_diaria

def selecionar_diarista():
    diarias = Diaria.objects.filter(status=2)
    for diaria in diarias:
        if verificar_diferenca_data_contratacao(diaria.created_at) > datetime.timedelta(hours=24):
            selecionar_diarista_diaria(diaria.id)