from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from api.models import Diaria

@login_required
def lista_diarias(request):
    diarias = Diaria.objects.all()
    return render(request, 'diarias/lista_diarias.html', {'diarias': diarias})


def transferir_pagamento_diaria(request, diaria_id):
    diaria = Diaria.objects.get(id=diaria_id)
    diaria.status = 7
    diaria.save()
    return HttpResponseRedirect(reverse('listar_diarias'))
