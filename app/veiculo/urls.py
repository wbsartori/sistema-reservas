from django.urls import path

from .views import veiculo, novo_veiculo, deletar_veiculo

urlpatterns = [
    path('', veiculo, name='veiculo'),
    path('veiculo/novo/', novo_veiculo, name='novo_veiculo'),
    path('veiculo/deletar/<int:id>', deletar_veiculo, name='deletar_veiculo'),
]