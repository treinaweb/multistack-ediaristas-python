from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..serializers.endereco_diarista_serializer import EnderecoDiaristaSerializer
from ..models import EnderecoDiarista
from ..permissions import diarista_permission

class EnderecoDiarista(APIView):
    permission_classes = [diarista_permission.DiaristaPermission, ]
    
    def put(self, request, format=None):
        serializer_endereco_diarista = \
        EnderecoDiaristaSerializer(data=request.data, context={'request': request})
        if serializer_endereco_diarista.is_valid():
            serializer_endereco_diarista.save()
            return Response(serializer_endereco_diarista.validated_data, 
            status=status_http.HTTP_201_CREATED)
        return Response(serializer_endereco_diarista.errors, 
        status=status_http.HTTP_400_BAD_REQUEST)