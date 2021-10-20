from rest_framework.response import Response
from rest_framework import serializers, status as status_htttp
from rest_framework.views import APIView
from ..serializers import avaliacao_diaria_serializer
from ..permissions import dono_permission
from ..models import AvaliacaoDiaria
from ..services import diaria_service, usuario_service


class AvaliacaoDiariaID(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def patch(self, request, diaria_id, format=None):
        diaria = diaria_service.listar_diaria_id(diaria_id)
        if diaria.status != 4:
            raise serializers.ValidationError(
                "Apenas diárias com status 4 podem ser avaliadas")
        usuario_logado = usuario_service.listar_usuario_id(request.user.id)
        self.check_object_permissions(self.request, diaria)
        serializer_avaliacao_diaria = avaliacao_diaria_serializer.AvaliacaoDiariaSerializer(
            data=request.data
        )
        # verificar se o usuário que está avaliando já não tinha avaliado anteriormente
        if serializer_avaliacao_diaria.is_valid():
            if usuario_logado.tipo_usuario == 1:
                avaliado = diaria.diarista
            else:
                avaliado = diaria.cliente
            serializer_avaliacao_diaria.save(visibilidade=1, diaria=diaria, 
            avaliador=usuario_logado, avaliado=avaliado)
            # atualizar a nota do usuário que está sendo avaliado
            # verificar se os dois usuários avaliaram
            # alterar o status da diária pra 6
            # retornar os dados da avaliação
