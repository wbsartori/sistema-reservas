from django.shortcuts import render

from reserva.models import Reserva
from .forms import ReservarVeiculoForm
# Create your views here.

def veiculo(request):
    return render(request, 'veiculos.html')

def novo_veiculo(request):
    form = ReservarVeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'novo_veiculos.html', context)