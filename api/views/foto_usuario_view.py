from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..serializers import foto_usuario_serializer
from ..services import usuario_service
from rest_framework import status as status_http

class FotoUsuario(APIView):
    def post(self, request, format=None):
        usuario = usuario_service.listar_usuario_id(request.user.id)
        serializer_foto_usuario = foto_usuario_serializer.FotoUsuarioSerailizer(
            data=request.data)
        if serializer_foto_usuario.is_valid():
            foto_usuario = serializer_foto_usuario.validated_data['foto_usuario']
            usuario.foto_usuario = foto_usuario
            usuario.save()
            return Response("Foto alterada com sucesso", status=status_http.HTTP_200_OK)
        return Response(serializer_foto_usuario.errors, status=status_http.HTTP_400_BAD_REQUEST)