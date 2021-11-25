from os import link
from django.urls.base import reverse
from rest_framework.views import APIView
from ..hateoas import Hateoas
from django.urls import reverse
from rest_framework.response import Response
from rest_framework import status as status_http

class Inicio(APIView):
    def get(self, request, format=None):
        links = Hateoas()
        links.add_get('listar_servicos', reverse('servico-list'))
        links.add_get('endereco_cep', reverse('endereco-cep-list'))
        links.add_get('diaristas_localidade', reverse('diaristas-localidades-list'))
        links.add_get('verificar_disponibilidade_atendimento', 
        reverse('disponibilidade-atendimento-cidade-list')),
        links.add_post('cadastrar_usuario', reverse('usuario-list')),
        links.add_post('login', reverse('token_obtain_pair')),
        links.add_post('logout', reverse('logout-list')),
        links.add_get('usuario_logado', reverse('me-list')),
        links.add_post('solicitar_alteracao_senha', 
        reverse('password_reset:reset-password-request'))
        links.add_post('confirmar_alteracao_senha', 
        reverse('password_reset:reset-password-confirm'))
        return Response({"links": links.to_array()}, status=status_http.HTTP_200_OK)
