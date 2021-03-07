from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from backend.models import AuthUser
from reserva.models import Reserva

from .forms import ReservarSalaForm


def sala(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()

    context = {
        'reservas': reservas,
        'usuarios': usuarios
    }
    return render(request, 'salas.html', context)


def novo_sala(request):
    form = ReservarSalaForm(request.POST)
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarSalaForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('sala.html')
    else:
        return render(request, 'novo_sala.html', context)