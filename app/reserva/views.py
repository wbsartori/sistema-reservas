from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from backend.models import AuthUser
from django.contrib import messages

def multiplo(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()

    context = {
        'reservas': reservas,
        'usuarios': usuarios
    }
    return render(request, 'multiplos.html', context)


def novo_multiplo(request):
    form = ReservarMultiplosForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarMultiplosForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/reserva/')
    else:
        return render(request, 'novo_multiplos.html', context)



def deletar_multiplos(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    messages.info(request, 'Reserva multipla deletada com sucesso!')
    return redirect('multiplo')