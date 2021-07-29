
from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import cidades_atendimento_service
from ..serializers import endereco_cep_serializer
from rest_framework import status as status_http

class EnderecoCep(APIView):
    def get(self, request, format=None):
        cep = self.request.query_params.get('cep', None)
        endereco = cidades_atendimento_service.buscar_cidade_cep(cep)
        serializer_endereco_cep = endereco_cep_serializer.EnderecoCepSerializer(endereco)
        return Response(serializer_endereco_cep.data, status=status_http.HTTP_200_OK)