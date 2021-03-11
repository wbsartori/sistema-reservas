from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', sala, name='sala'),
    path('novo_sala/', novo_sala, name='novo_sala'),
    path('sala/deletar/<int:id>', deletar_sala, name='deletar_sala'),
]