from rest_framework import permissions

class EditarUsuarioPermission(permissions.BasePermission):
    message = 'Você deve estar autenticado'

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_authenticated