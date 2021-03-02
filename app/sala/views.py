from django.shortcuts import render

from .forms import ReservarSalaForm

# Create your views here.
def sala(request):
    return render(request, 'salas.html')

def novo_sala(request):
    form = ReservarSalaForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }

    return render(request, 'novo_sala.html', context)