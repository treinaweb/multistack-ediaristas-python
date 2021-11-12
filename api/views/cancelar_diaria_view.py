from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..permissions import dono_permission
from ..serializers import cancelar_diaria_serializer
from ..services import diaria_service, cancelar_diaria_service


class CancelarDiariaID(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def patch(self, request, diaria_id, format=None):
        serializer_cancelar_diaria = cancelar_diaria_serializer.CancelarDiariaSerializer(
                                                                        data=request.data)
        diaria = diaria_service.listar_diaria_id(diaria_id)
        self.check_object_permissions(self.request, diaria)
        if serializer_cancelar_diaria.is_valid():
            cancelar_diaria_service.cancelar_diaria(diaria_id, request.user.id)
            diaria_service.atualizar_status_diaria(diaria_id, 5)
            return Response("Diária cancelada com sucesso", status=status_http.HTTP_200_OK)
        return Response(serializer_cancelar_diaria.errors, status=status_http.HTTP_400_BAD_REQUEST)