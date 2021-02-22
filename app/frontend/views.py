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