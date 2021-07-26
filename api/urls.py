from django.urls import path
from .views import diaristas_localidade_view

urlpatterns = [
    path('diaristas/localidades', diaristas_localidade_view.DiaristasLocalidades.as_view(),
    name='diaristas-localidades-list')
]