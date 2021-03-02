from django.shortcuts import render
from .forms import *
from .models import *
from backend.models import AuthUser

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
            return render(request, 'multiplos.html')

    return render(request, 'novo_multiplos.html', context)
