import requests
import json
from rest_framework import serializers
from ..models import CidadesAtendimento
from .usuario_service import listar_usuario_id


def cadastrar_cidade(codigo_ibge, cidade, estado):
    return CidadesAtendimento.objects.get_or_create(codigo_ibge=codigo_ibge,
    defaults=dict(
        cidade=cidade,
        estado=estado
    ))

def listar_diaristas_cidade(cep):
    codigo_ibge = buscar_cidade_cep(cep)['ibge']
    try:
        cidade = CidadesAtendimento.objects.get(codigo_ibge=codigo_ibge)
        return cidade.usuario.filter(tipo_usuario=2).order_by('-reputacao')
    except CidadesAtendimento.DoesNotExist:
        return []

def verificar_disponibilidade_cidade(cep):
    codigo_ibge = buscar_cidade_cep(cep)['ibge']
    return CidadesAtendimento.objects.filter(codigo_ibge=codigo_ibge).exists()

def relacionar_cidade_diarista(usuario, cidades):
    usuario_relacionar = listar_usuario_id(usuario.id)
    usuario_relacionar.cidades_atendidas.clear()
    for cidade in cidades.value:
        dados_api = buscar_cidade_ibge(cidade['codigo_ibge'])
        cidade_nova, create = cadastrar_cidade(cidade['codigo_ibge'], dados_api['nome'],
        dados_api['microrregiao']['mesorregiao']['UF']['sigla'])
        usuario_relacionar.cidades_atendidas.add(cidade_nova.id)


def buscar_cidade_cep(cep):
    requisicao = requests.get(
        f"https://viacep.com.br/ws/{cep}/json/"
    )

    if requisicao.status_code == 400:
        raise serializers.ValidationError({"detail": "Erro ao buscar o CEP"})
    cidade_api = json.loads(requisicao.content)
    if 'erro' in cidade_api:
        raise serializers.ValidationError({"detail": "O CEP informado não foi encontrado"})
    return cidade_api

def buscar_cidade_ibge(ibge):
    requisicao = requests.get(
        f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{ibge}"
    )
    if len(requisicao.content) == 2:
        raise serializers.ValidationError("A cidade não existe")
    cidade_api = json.loads(requisicao.content)
    return cidade_api