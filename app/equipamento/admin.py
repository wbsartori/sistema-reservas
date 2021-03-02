from django.contrib import admin
from .models import *

class EquipamentoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(EquipamentoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class EquipamentoMarcaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(EquipamentoMarcaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class EquipamentoTipoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(EquipamentoTipoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

admin.site.register(Equipamento)
admin.site.register(EquipamentoMarca, EquipamentoMarcaAdmin)
admin.site.register(EquipamentoTipo, EquipamentoTipoAdmin)