from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from backend.models import AuthUser
from reserva.models import Reserva
from django.contrib import messages
from .forms import ReservarEquipamentoForm


@login_required
def equipamento(request):
    reservas = Reserva.objects.all()
    usuarios = AuthUser.objects.all()

    context = {
        'reservas': reservas,
        'usuarios': usuarios
    }
    return render(request, 'equipamentos.html', context)


@login_required
def novo_equip(request):
    form = ReservarEquipamentoForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ReservarEquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/equipamento/')

    return render(request, 'novo_equip.html',context)

@login_required
def deletar_equip(request, id):
    reserva = get_object_or_404(Reserva, pk=id)
    reserva.delete()
    messages.info(request, 'Reserva de equipamento deletada com sucesso!')
    return redirect('equipamento')