from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..permissions import dono_permission
from ..serializers import cancelar_diaria_serializer
from ..services import diaria_service


class CancelarDiariaID(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def patch(self, request, diaria_id, format=None):
        serializer_cancelar_diaria = cancelar_diaria_serializer.CancelarDiariaSerializer(
                                                                        data=request.data)
        diaria = diaria_service.listar_diaria_id(diaria_id)
        self.check_object_permissions(self.request, diaria)
        if serializer_cancelar_diaria.is_valid():
            # iniciar a lógica de negócio
            # alterar o status da diária pra 5
            # retornar mensagem de cancelamento feito com sucesso
        