from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('sala/', sala, name='sala'),
    path('sala/novo/', novo_sala, name='novo_sala'),
]