import datetime

from ..models import Diaria
from ..services import pagamento_diaria_service, cancelar_diaria_service

def cancelar_diaria_task():
    diarias = Diaria.objects.filter(status=2)
    for diaria in diarias:
        if not diaria.candidatas.exists():
            if cancelar_diaria_service.verificar_diferenca_data_atual(
                diaria.data_atendimento) <= datetime.timedelta(hours=24):
                    pagamento_diaria_service.cancelar_pagamento(diaria.id, False)
                    diaria.status = 5
                    diaria.save()
