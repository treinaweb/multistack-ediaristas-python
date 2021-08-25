from rest_framework import permissions

class ClientePermission(permissions.BasePermission):

    message = 'Você não possui permissão para acessar este dado.'

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.tipo_usuario == 1

    
    def has_object_permission(self, request, view, obj):
        return request.user == obj.cliente