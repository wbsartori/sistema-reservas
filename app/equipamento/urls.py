from django.urls import path

from .views import *

urlpatterns = [
    path('', equipamento, name='equipamento'),
    path('equipamento/novo/', novo_equip, name='novo_equip'),
    path('/equipamento/deletar/<int:id>', deletar_equip, name='deletar_equip'),
]