from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import usuario_serializer


class Usuario(APIView):
    def post(self, request, format=None):
        serializer_usuario = usuario_serializer.UsuarioSerializer(data=request.data,
                                                            context={"request": request})
        if serializer_usuario.is_valid():
            usuario_criado = serializer_usuario.save()
            serializer_usuario = usuario_serializer.UsuarioSerializer(usuario_criado)
            return Response(serializer_usuario.data)
        return Response(serializer_usuario.errors)