from django.urls import path

from .views import *

urlpatterns = [
    path('', multiplo, name='multiplo'),
    path('multiplo/novo/', novo_multiplo, name='novo_multiplo'),
    path('multiplo/deletar/<int:id>', deletar_multiplos, name='deletar_multiplos'),
]
