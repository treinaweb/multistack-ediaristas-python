from ..models import Servico

def listar_servicos():
    return Servico.objects.order_by('posicao')