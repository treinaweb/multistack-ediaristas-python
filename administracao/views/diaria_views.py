from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from api.models import Diaria

@login_required
def lista_diarias(request):
    diarias = Diaria.objects.all()
    return render(request, 'diarias/lista_diarias.html', {'diarias': diarias})
