from django.db import models
from django.db.models import Count

class DiariaManager(models.Manager):
    def oportunidades_cidade(self, codigos_ibge):
        return self.get_queryset().annotate(numero_diarista=Count('candidatas')).filter(
            codigo_ibge__in=codigos_ibge).filter(status=2)