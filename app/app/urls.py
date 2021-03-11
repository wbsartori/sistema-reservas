"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from home import urls as index_url
from equipamento import urls as url_equip
from sala import urls as url_sala
from veiculo import urls as url_veiculo
from reserva import urls as url_reserva

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(index_url)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('equipamento/', include(url_equip)),
    path('sala/', include(url_sala)),
    path('veiculo/', include(url_veiculo)),
    path('reserva/', include(url_reserva)),
]
