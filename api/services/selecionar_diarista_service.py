from .diaria_service import listar_diaria_id, calcular_indice_compatibilidade
from ..services import candidatar_diarista_diaria_service

def selecionar_diarista_diaria(diaria_id):
    diaria = listar_diaria_id(diaria_id)
    candidatas = diaria.candidatas.all()
    diarista_compativel = []
    for candidata in candidatas:
        indice = calcular_indice_compatibilidade(diaria.id, candidata.id)
        diarista_compativel.append(indice)
    diarista = diarista_compativel.index(max(diarista_compativel))
    candidatar_diarista_diaria_service.contratar_diarista_diaria(diaria, candidatas[diarista].id)


    
