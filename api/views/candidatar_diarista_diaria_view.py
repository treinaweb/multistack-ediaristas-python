from rest_framework.views import APIView
from permissions.diarista_permission import DiaristaPermission
from rest_framework.response import Response
from rest_framework import status as status_http


class CandidatarDiaristaDiaria(APIView):
    permission_classes = [DiaristaPermission, ]

    def post(self, request, diaria_id, format=None):
        # metodo para relacionar o diarista com a diaria
        return Response({"Candidatura realizada com sucesso"}, 
        status=status_http.HTTP_201_CREATED)

