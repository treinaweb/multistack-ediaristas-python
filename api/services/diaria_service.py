from rest_framework import serializers
from ..models import Diaria
from .usuario_service import listar_usuario_id
from .endereco_diarista_service import listar_endereco_diarista
import datetime
import googlemaps

def listar_diaria_id(diaria_id):
    return Diaria.objects.get(id=diaria_id)


def atualizar_status_diaria(diaria_id, status):
    diaria = listar_diaria_id(diaria_id)
    diaria.status = status
    diaria.save()


def listar_diarias_usuario(usuario_id):
    usuario = listar_usuario_id(usuario_id)
    if usuario.tipo_usuario == 1:
        return Diaria.objects.filter(cliente=usuario.id).all()
    return Diaria.objects.filter(diarista=usuario.id).all()


def calcular_indice_compatibilidade(diaria_id, diarista_id):
    diaria = listar_diaria_id(diaria_id)
    diarista = listar_usuario_id(diarista_id)
    reputacao_diarista = diarista.reputacao
    endereco_diarista = listar_endereco_diarista(diarista_id)
    distancia_diarista_diaria = calcular_distancia_diaria_diarista(diaria.cep, 
                                                                    endereco_diarista.cep)
    return (reputacao_diarista - (distancia_diarista_diaria/10)) / 2


def calcular_distancia_diaria_diarista(cep_diaria, cep_diarista):
    gmaps = googlemaps.Client(key='AIzaSyBq4s9zZ5X6zBju0pe5HtsEO_S-2gy4sBs')
    cep_formatado_diaria = cep_diaria[:5] + '-' + cep_diaria[5:]
    cep_formatado_diarista = cep_diarista[:5] + '-' + cep_diarista[5:]
    distancia = gmaps.distance_matrix(
                    cep_formatado_diaria, cep_formatado_diarista
                )['rows'][0]['elements'][0]
    if distancia['status'] == 'ZERO_RESULTS':
        raise serializers.ValidationError("Erro ao calcular a distância")
    return distancia['distance']['value']


def confirmar_presenca_diarista(diaria_id):
    diaria = listar_diaria_id(diaria_id)
    if diaria.status != 3:
        raise serializers.ValidationError(
                "Só é possível executar essa ação em diárias com status 3"
                )
    data_atual = datetime.datetime.now()
    data_diaria = diaria.data_atendimento.replace(tzinfo=None)
    if data_atual <= data_diaria:
        raise serializers.ValidationError(
                "A data atual não pode ser menor que a data de atendimento"
            )
    diaria.status = 4
    diaria.save()

