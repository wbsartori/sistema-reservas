from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def equipamento(request):
    return render(request, 'equipamentos/equipamentos.html')

def sala(request):
    return render(request, 'salas/salas.html')

def veiculo(request):
    return render(request, 'veiculos/veiculos.html')

def multiplo(request):
    return render(request, 'reservas/multiplos.html')

def novo_equip(request):
    return render(request,'equipamentos/novo_equip.html')

def novo_sala(request):
    return render(request,'salas/novo_sala.html')

def novo_multiplo(request):
    return render(request,'reservas/novo_multiplos.html')

def novo_veiculo(request):
    return render(request,'veiculos/novo_veiculos.html')