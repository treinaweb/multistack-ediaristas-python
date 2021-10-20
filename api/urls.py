from django.urls import path
from .views import (diaristas_localidade_view, endereco_cep_view, 
                    disponibilidade_atendimento_cidade,
                    servico_view, inicio_view, usuario_view, me_view,
                    diaria_view, pagamento_diaria_view, endereco_diarista_view,
                    cidades_atendimento_diarista_view, oportunidade_view,
                    candidatar_diarista_diaria_view, confirmar_presenca_diarista_view,
                    avaliacao_diaria_view)



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

    path('usuarios/enderecos', endereco_diarista_view.EnderecoDiarista.as_view(), 
    name='endereco-diarista-detail'),

    path('me', me_view.Me.as_view(), name='me-list'),

    path('diarias', diaria_view.Diaria.as_view(), name='diaria-list'),

    path('diarias/<int:diaria_id>', diaria_view.DiariaID.as_view(), name='diaria-detail'),

    path('diarias/<int:diaria_id>/candidatar', 
    candidatar_diarista_diaria_view.CandidatarDiaristaDiaria.as_view(),
    name='candidatar-diarista-diaria-list'),

    path('diarias/<int:diaria_id>/pagamentos', pagamento_diaria_view.PagamentoDiaria.as_view(),
    name='pagamento-diaria-list'),

    path('diarias/<int:diaria_id>/confirmar-presenca', 
    confirmar_presenca_diarista_view.ConfirmarPresencaDiaristaID.as_view(), 
    name='confirmar-presenca-diaria-detail'),

    path('diarias/<int:diaria_id>/avaliacao',
    avaliacao_diaria_view.AvaliacaoDiariaID.as_view(),
    name='avaliacao-diaria-detail'),

    path('usuarios/cidades-atendidas', 
    cidades_atendimento_diarista_view.CidadesAtendimentoDiaristaID.as_view(),
    name='cidades-atendimento-diarista-detail'),

    path('oportunidades', oportunidade_view.Oportunidade.as_view(), name='oportunidade-list')

]