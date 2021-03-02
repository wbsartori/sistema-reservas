from django.contrib import admin
from .models import *


class ReservaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(ReservaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('id_usuario')
        return queryset


admin.site.register(Reserva,ReservaAdmin)