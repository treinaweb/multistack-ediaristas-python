from django.db.models.signals import post_save
from .models import Usuario

def usuario_cadastrado(sender, instance, created, **kwargs):
    print("Usuário cadastrado")
    print(instance.nome_completo)

post_save.connect(usuario_cadastrado, sender=Usuario)

