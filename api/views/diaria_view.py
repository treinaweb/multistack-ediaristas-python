from rest_framework import response
from rest_framework.views import APIView
from ..serializers import diaria_serializer
from rest_framework.response import Response
from rest_framework import status as status_http
from rest_framework import permissions
from rest_framework import serializers
from ..services.diaria_service import listar_diarias_usuario, listar_diaria_id
from ..permissions import dono_permission

class Diaria(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, format=None):
        diarias = listar_diarias_usuario(request.user.id)
        serializer_diaria = diaria_serializer.DiariaSerializer(diarias, many=True,
        context={'request': request})
        return Response(serializer_diaria.data, status=status_http.HTTP_200_OK)


    def post(self, request, format=None):
        serializer_diaria = diaria_serializer.DiariaSerializer(data=request.data,
        context={'request': request})
        if request.user.tipo_usuario == 2:
            raise serializers.ValidationError("Apenas clientes podem solicitar diárias")
        if serializer_diaria.is_valid():
            serializer_diaria.save()
            return Response(serializer_diaria.data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_diaria.errors, status=status_http.HTTP_400_BAD_REQUEST)


class DiariaID(APIView):
    permission_classes = [dono_permission.DonoPermission, ]

    def get(self, request, diaria_id, format=None):
        diaria = listar_diaria_id(diaria_id)
        self.check_object_permissions(self.request, diaria)
        serializer_diaria = diaria_serializer.DiariaSerializer(diaria, 
        context={'request': request})
        return Response(serializer_diaria.data, status=status_http.HTTP_200_OK)