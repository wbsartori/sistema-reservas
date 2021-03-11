from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from reserva.models import Reserva
from backend.models import AuthUser
from django.http import HttpResponseRedirect
from .models import VeiculoMarca, VeiculoModelo, Veiculo
from .forms import ReservarVeiculoForm
from django.contrib import messages


@login_required
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


@login_required
def novo_veiculo(request):
    form = ReservarVeiculoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/veiculo/')

    return render(request, 'novo_veiculos.html', context)


@login_required
def deletar_veiculo(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    messages.info(request, 'Reserva de veiculo deletada com sucesso!')
    return redirect('/veiculo')

