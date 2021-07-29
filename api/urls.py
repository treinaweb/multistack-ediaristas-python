from django.urls import path
from .views import (diaristas_localidade_view, endereco_cep_view, 
                    disponibilidade_atendimento_cidade,
                    servico_view)



urlpatterns = [
    path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(),
    name='diaristas-localidades-list'),
    path('enderecos', endereco_cep_view.EnderecoCep.as_view(),
    name='endereco-cep-list'),
    path('diaristas/disponibilidade', 
    disponibilidade_atendimento_cidade.DisponibilidadeAtendimentoCidade.as_view(),
    name='disponibilidade-atendimento-cidade-list'),
    path('servicos', servico_view.Servico.as_view(), name='servico-list'),
    path('servicos/<int:servico_id>', servico_view.ServicoId.as_view(),
    name='servico-detail')
]