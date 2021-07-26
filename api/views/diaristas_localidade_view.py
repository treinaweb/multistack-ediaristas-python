from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadesSerializer
from rest_framework import status as status_http
from ..services import cidades_atendimento_service
from ..paginations import diaristas_localidade_pagination


class DiaristasLocalidades(APIView, 
diaristas_localidade_pagination.DiaristasLocalidadePagination):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        diaristas = cidades_atendimento_service.listar_diaristas_cidade(cep)
        resultado = self.paginate_queryset(diaristas, request)
        serializer_diaristas_localidade = DiaristasLocalidadesSerializer(
                                            resultado, many=True, 
                                            context={"request": request})
        return self.get_paginated_response(serializer_diaristas_localidade.data)