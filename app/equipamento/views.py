from django.shortcuts import render

from .forms import ReservarEquipamentoForm

def equipamento(request):
    return render(request, 'equipamentos.html')

def novo_equip(request):
    form = ReservarEquipamentoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'novo_equip.html', context)
