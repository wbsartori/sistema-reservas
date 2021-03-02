from django.shortcuts import render
from backend.models import AuthUser
from reserva.models import Reserva

from .forms import ReservarEquipamentoForm

def equipamento(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()

    context = {
        'reservas': reservas,
        'usuarios': usuarios
    }
    return render(request, 'equipamentos.html', context)

def novo_equip(request):
    form = ReservarEquipamentoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'equipamentos.html', context)

    return render(request, 'novo_equip.html', context)
