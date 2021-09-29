from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..serializers import (cidades_atendimento_diarista_serializer, 
relacionar_cidade_diarista_serializer)
from ..services import usuario_service, cidades_atendimento_service
from ..permissions import diarista_permission

class CidadesAtendimentoDiaristaID(APIView):
    permission_classes = [diarista_permission.DiaristaPermission, ]
    def put(self, request, format=None):
        serializer_cidades_atendimento = relacionar_cidade_diarista_serializer\
            .RelacionarCidadeDiaristaSerializer(data=request.data)
        usuario = usuario_service.listar_usuario_id(request.user.id)
        if serializer_cidades_atendimento.is_valid():
            cidades = serializer_cidades_atendimento["cidades"]
            cidades_atendimento_service.relacionar_cidade_diarista(usuario, cidades)
            return Response(serializer_cidades_atendimento.data, 
            status=status_http.HTTP_201_CREATED)
        return Response(serializer_cidades_atendimento.errors, 
        status=status_http.HTTP_400_BAD_REQUEST)

