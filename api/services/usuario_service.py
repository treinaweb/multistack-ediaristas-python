from ..models import Usuario

def listar_usuario_email(email):
    return Usuario.objects.get(email=email)


def listar_usuario_id(id):
    return Usuario.objects.get(id=id)