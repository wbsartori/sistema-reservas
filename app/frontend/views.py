from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'home/index.html')

def equipamento(request):
    return render(request, 'reservas/equipamentos.html')

def sala(request):
    return render(request, 'reservas/salas.html')

def veiculo(request):
    return render(request, 'reservas/veiculos.html')

def multiplo(request):
    return render(request, 'reservas/multiplos.html')