from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('equipamento/', equipamento, name='equipamento'),
    path('equipamento/novo/', novo_equip, name='novo_equip'),
    path('sala/', sala, name='sala'),
    path('sala/novo/', novo_sala, name='novo_sala'),
    path('veiculo/', veiculo, name='veiculo'),
    path('veiculo/novo/', novo_veiculo, name='novo_veiculo'),
    path('multiplo/', multiplo, name='multiplo'),
    path('multiplo/novo/', novo_multiplo, name='novo_multiplo'),
]
