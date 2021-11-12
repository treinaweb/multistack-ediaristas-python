import datetime

from rest_framework import serializers
from ..services import diaria_service, usuario_service

def cancelar_diaria(diaria_id, usuario_id):
    diaria = diaria_service.listar_diaria_id(diaria_id)
    usuario = usuario_service.listar_usuario_id(usuario_id)
    if not (diaria.status == 2 or diaria.status == 3):
        raise serializers.ValidationError("Esta diária não pode ser cancelada")
    verificar_data_cancelamento(diaria.data_atendimento)
    sem_penalidade = verificar_penalizacao_cancelamento(diaria.data_atendimento)
    

def verificar_penalizacao_cancelamento(data_diaria):
    return verificar_diferenca_data_atual(data_diaria) > datetime.timedelta(hours=24)


def verificar_data_cancelamento(data_diaria):
    data_atual = datetime.datetime.now()
    data_diaria_cancelar = data_diaria.replace(tzinfo=None)
    if data_atual > data_diaria_cancelar:
        raise serializers.ValidationError("Não é possível cancelar a diária."
                                            "Entre em contato com o nosso suporte")
    return data_diaria

def verificar_diferenca_data_atual(data_diaria):
    data_atual = datetime.datetime.now()
    data_diaria_cancelar = data_diaria.replace(tzinfo=None)
    return abs(data_diaria_cancelar - data_atual)
