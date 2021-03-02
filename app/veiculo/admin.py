from django.contrib import admin
from .models import *

# Register your models here.
class VeiculoCorAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(VeiculoCorAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class VeiculoMarcaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(VeiculoMarcaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset


class VeiculoModeloAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(VeiculoModeloAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class VeiculoTipoCombustivelAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(VeiculoTipoCombustivelAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class VeiculoTipoVeiculoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(VeiculoTipoVeiculoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

admin.site.register(Veiculo)
admin.site.register(VeiculoCor, VeiculoCorAdmin)
admin.site.register(VeiculoMarca, VeiculoMarcaAdmin)
admin.site.register(VeiculoModelo, VeiculoModeloAdmin)
admin.site.register(VeiculoTipoCombustivel,VeiculoTipoCombustivelAdmin)
admin.site.register(VeiculoTipoVeiculo,VeiculoTipoVeiculoAdmin)