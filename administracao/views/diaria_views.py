from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse
from api.models import Diaria

@login_required
def lista_diarias(request):
    status = request.GET.get('status', None)
    if status is None:
        status_diaria = [2, ]
    elif status == 'pendentes':
        status_diaria = [3, ]
    elif status == 'nao-avaliadas':
        status_diaria = [4, ]
    elif status == 'canceladas':
        status_diaria = [5, 1]
    else:
        status_diaria = [6, 7]
    diarias = Diaria.objects.filter(status__in=status_diaria)
    return render(request, 'diarias/lista_diarias.html', {'diarias': diarias})


def transferir_pagamento_diaria(request, diaria_id):
    diaria = Diaria.objects.get(id=diaria_id)
    diaria.status = 7
    diaria.save()
    return HttpResponseRedirect(reverse('listar_diarias'))
