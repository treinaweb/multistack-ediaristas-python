from django.db import models
from django.db.models import Avg

class AvaliacaoManager(models.Manager):
    def reputacao_usuario(self, usuario_id):
        return self.get_queryset().filter(avaliado=usuario_id).aggregate(Avg('nota'))