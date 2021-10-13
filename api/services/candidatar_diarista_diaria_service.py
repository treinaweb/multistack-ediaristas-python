import datetime
from ..models import Diaria, Usuario
from rest_framework import serializers
from .selecionar_diarista_service import selecionar_diarista_diaria

def relacionar_candidata_diaria(diaria_id, diarista_id):
    diaria = Diaria.diaria_objects.diaristas_diaria(diaria_id)
    diarista = Usuario.objects.get(id=diarista_id)
    if verificar_diferenca_data_contratacao(diaria.created_at) > datetime.timedelta(hours=24):
        contratar_diarista_diaria(diaria, diarista_id)
        return 
    if diaria.candidatas__count >= 3:
        raise serializers.ValidationError("A diária já possui 3 candidatas")
    if diaria.candidatas__count < 2:
        diaria.candidatas.add(diarista)
    if diaria.candidatas__count == 2:
        diaria.candidatas.add(diarista)
        selecionar_diarista_diaria(diaria.id)


def contratar_diarista_diaria(diaria, diarista_id):
    if diaria.status != 2:
        raise serializers.ValidationError("Apenas diárias pagas podem ser realizadas")
    diarista = Usuario.objects.get(id=diarista_id)
    diaria.diarista = diarista
    diaria.status = 3
    diaria.save()

def verificar_diferenca_data_contratacao(data_diaria):
    data_atual = datetime.datetime.now()
    data_diaria_criacao = data_diaria.replace(tzinfo=None)
    diferenca = data_atual - data_diaria_criacao
    return abs(diferenca)