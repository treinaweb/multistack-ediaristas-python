import datetime

from django.db.models.aggregates import Count

from ..models import Diaria
from ..services.candidatar_diarista_diaria_service import verificar_diferenca_data_contratacao
from ..services.selecionar_diarista_service import selecionar_diarista_diaria

def selecionar_diarista():
    diarias = Diaria.objects.annotate(
        candidatas_count=Count('candidatas')
        ).filter(candidatas_count__gt=1).filter(status=2)
    for diaria in diarias:
        if verificar_diferenca_data_contratacao(diaria.created_at) > datetime.timedelta(hours=24):
            selecionar_diarista_diaria(diaria.id)