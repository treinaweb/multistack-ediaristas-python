from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..models import Diaria, Pagamento as PagamentoModel
from ..serializers import pagamento_serializer
from ..permissions import diarista_permission

class Pagamento(APIView):
    permission_classes = [diarista_permission.DiaristaPermission, ]
    def get(self, request, format=None):
        diarias_pagamento = Diaria.objects.filter(diarista=request.user.id).filter(
            status__in=[4, 6, 7])
        pagamentos = PagamentoModel.objects.filter(diaria__in=diarias_pagamento)
        serializer_pagamento = pagamento_serializer.PagamentoSerializer(pagamentos, many=True)
        return Response(serializer_pagamento.data, status=status_http.HTTP_200_OK)