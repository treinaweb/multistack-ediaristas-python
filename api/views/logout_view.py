from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status as status_http
from rest_framework import permissions

class Logout(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status_http.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status_http.HTTP_400_BAD_REQUEST)