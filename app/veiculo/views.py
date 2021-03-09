from django.shortcuts import render, redirect, get_object_or_404

from reserva.models import Reserva
from backend.models import AuthUser
from .models import VeiculoMarca, VeiculoModelo, Veiculo
from .forms import ReservarVeiculoForm
from django.contrib import messages
# Create your views here.

def veiculo(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()
    veiculosMarca = VeiculoMarca.objects.all()
    veiculosModelo = VeiculoModelo.objects.all()
    veiculo = Veiculo.objects.all()

    context = {
        'reservas': reservas,
        'usuarios' : usuarios,
        'veiculosMarca': veiculosMarca,
        'veiculoModelo': veiculosModelo,
        'veiculo': veiculo
    }
    return render(request, 'veiculos.html', context)

def novo_veiculo(request):
    form = ReservarVeiculoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarVeiculoForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect('/veiculo')

    return render(request, 'novo_veiculos.html', context)

def deletar_veiculo(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    messages.info(request, 'Reserva de veiculo deletada com sucesso!')
    return redirect('/veiculo')

