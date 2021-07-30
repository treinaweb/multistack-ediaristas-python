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
        reverse('disponibilidade-atendimento-cidade-list'))
        return Response({"links": links.to_array()}, status=status_http.HTTP_200_OK)
