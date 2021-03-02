from django.urls import path

from .views import *

urlpatterns = [
    path('multiplo/', multiplo, name='multiplo'),
    path('multiplo/novo/', novo_multiplo, name='novo_multiplo'),
]
