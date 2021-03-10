from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from backend.models import AuthUser
from reserva.models import Reserva
from django.contrib import messages
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
    form = ReservarSalaForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarSalaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sala/')

    return render(request, 'novo_sala.html', context)


def deletar_sala(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    messages.info(request, 'Reserva de sala deletada com sucesso!')
    return redirect('sala')