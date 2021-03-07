from django.urls import path

from .views import veiculo, novo_veiculo

urlpatterns = [
    path('', veiculo, name='veiculo'),
    path('veiculo/novo/', novo_veiculo, name='novo_veiculo'),
]