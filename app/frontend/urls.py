from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('equipamento/', equipamento, name='equipamento'),
    path('sala/', sala, name='sala'),
    path('veiculo/', veiculo, name='veiculo'),
    path('multiplo/', multiplo, name='multiplo'),
]
