from ..models import Servico
from django.http import Http404

def listar_servicos():
    return Servico.objects.order_by('posicao')

def listar_servico_id(servico_id):
    try:
        servico = Servico.objects.get(id=servico_id)
    except Servico.DoesNotExist:
        raise Http404
    return servico