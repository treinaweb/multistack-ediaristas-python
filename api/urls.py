from django.urls import path
from .views import (diaristas_localidade_view, endereco_cep_view, 
                    disponibilidade_atendimento_cidade,
                    servico_view, inicio_view, usuario_view, me_view,
                    diaria_view, pagamento_diaria_view)



urlpatterns = [
    path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(),
    name='diaristas-localidades-list'),

    path('enderecos', endereco_cep_view.EnderecoCep.as_view(),
    name='endereco-cep-list'),

    path('diaristas/disponibilidade', 
    disponibilidade_atendimento_cidade.DisponibilidadeAtendimentoCidade.as_view(),
    name='disponibilidade-atendimento-cidade-list'),

    path('servicos', servico_view.Servico.as_view(), name='servico-list'),

    path('', inicio_view.Inicio.as_view(), name='inicio'),

    path('usuarios', usuario_view.Usuario.as_view(), name='usuario-list'),

    path('me', me_view.Me.as_view(), name='me-list'),

    path('diarias', diaria_view.Diaria.as_view(), name='diaria-list'),

    path('diarias/<int:diaria_id>/pagamentos', pagamento_diaria_view.PagamentoDiaria.as_view(),
    name='pagamento-diaria-list')

]