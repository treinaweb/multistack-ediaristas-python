from django.db import models
from django.db.models import Avg

class DiaristaManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tipo_usuario=2)

    def reputacao_geral(self):
        return self.get_queryset().all().aggregate(Avg('reputacao'))