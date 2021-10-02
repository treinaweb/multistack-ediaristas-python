from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..serializers import oportunidade_serializer
from ..permissions import diarista_permission
from ..services import oportunidade_service

class Oportunidade(APIView):
    permission_classes = [diarista_permission.DiaristaPermission, ]

    def get(self, request, format=None):
        oportunidades = oportunidade_service.listar_oportunidades(request.user.id)
        serializer_oportunidade = oportunidade_serializer.OportunidadeSerializer(
                                    oportunidades, many=True, context={'request': request}
                                    )
        return Response(serializer_oportunidade.data, status=status_http.HTTP_200_OK)