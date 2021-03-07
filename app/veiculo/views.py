from django.shortcuts import render

from reserva.models import Reserva
from backend.models import AuthUser
from .models import VeiculoMarca, VeiculoModelo
from .forms import ReservarVeiculoForm
# Create your views here.

def veiculo(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()
    veiculosMarca = VeiculoMarca.objects.all()
    veiculosModelo = VeiculoModelo.objects.all()

    context = {
        'reservas': reservas,
        'usuarios' : usuarios,
        'veiculosMarca': veiculosMarca,
        'veiculoModelo': veiculosModelo
    }
    return render(request, 'veiculos.html', context)

def novo_veiculo(request):
    form = ReservarVeiculoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarVeiculoForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, 'veiculos.html', context)

    return render(request, 'novo_veiculos.html', context)