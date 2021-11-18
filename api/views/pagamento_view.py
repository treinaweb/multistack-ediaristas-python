from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..models import Diaria, Pagamento

class Pagamento(APIView):
    def get(self, request, format=None):
        diarias_pagamento = Diaria.objects.filter(diarista=request.user.id).filter(
            status__in=[4, 6, 7])
        pagamentos = Pagamento.objects.filter(diaria__in=diarias_pagamento)
        # serializar os dados
        # retoar os pagamentos do usuário