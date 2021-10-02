from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..serializers import oportunidade_serializer
from ..permissions import diarista_permission

class Oportunidade(APIView):
    permission_classes = [diarista_permission.DiaristaPermission, ]

    def get(self, request, format=None):
        # oportunidades = pegar lá do service a partir do usuário logado
        serializer_oportunidade = oportunidade_serializer.OportunidadeSerializer(
                                    opotunidades, many=True, context={'request': request}
                                    )
        return Response(serializer_oportunidade.data, status=status_http.HTTP_200_OK)