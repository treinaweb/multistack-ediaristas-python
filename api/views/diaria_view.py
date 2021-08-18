from rest_framework.views import APIView
from ..serializers import diaria_serializer
from rest_framework.response import Response
from rest_framework import status as status_http

class Diaria(APIView):
    def post(self, request, format=None):
        serializer_diaria = diaria_serializer.DiariaSerializer(data=request.data,
        context={'request': request})
        if serializer_diaria.is_valid():
            serializer_diaria.save()
            return Response(serializer_diaria.data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_diaria.errors, status=status_http.HTTP_400_BAD_REQUEST)