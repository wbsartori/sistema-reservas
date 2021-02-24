from django.shortcuts import render
from backend.models import Reserva
from .forms import ReservarEquipamentoForm, ReservarSalaForm, ReservarVeiculoForm, ReservarMultiplosForm

def index(request):
    return render(request, 'home/index.html')

def equipamento(request):
    return render(request, 'equipamentos/equipamentos.html')

def sala(request):
    return render(request, 'salas/salas.html')

def veiculo(request):
    return render(request, 'veiculos/veiculos.html')

def novo_veiculo(request):
    form = ReservarVeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request,'veiculos/novo_veiculos.html', context)

def novo_equip(request):
    form = ReservarEquipamentoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request,'equipamentos/novo_equip.html', context)


def novo_sala(request):
    form = ReservarSalaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request,'salas/novo_sala.html', context)

def novo_multiplo(request):
    form = ReservarMultiplosForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarMultiplosForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'reservas/multiplos.html')

    return render(request,'reservas/novo_multiplos.html', context)


def multiplo(request):
    reservas = Reserva.objects.all()
    context = {
        'reservas': reservas
    }
    return render(request, 'reservas/multiplos.html', context)
