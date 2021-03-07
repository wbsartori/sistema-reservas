from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', sala, name='sala'),
    path('novo_sala/', novo_sala, name='novo_sala'),
]