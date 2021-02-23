from django.contrib import admin
from .models import *

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('descricao','uf')

    def get_queryset(self, request):
        queryset = super(EstadoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class cidadeAdmin(admin.ModelAdmin):
    list_display = ('codigo_ibge','cidade')

    def get_queryset(self, request):
        queryset = super(cidadeAdmin, self).get_queryset(request)
        queryset = queryset.order_by('cidade')
        return queryset


class departamentoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(departamentoAdmin, self).get_queryset(request)
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

class EmpEmpresaAdmin(admin.ModelAdmin):

    list_display = ('codigo', 'descricao','endereco','numero','bairro','cep','cidade','uf')

    def get_queryset(self, request):
        queryset = super(EmpEmpresaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset


class EmpFilialAdmin(admin.ModelAdmin):

    list_display = ('codigo', 'descricao','endereco','numero','bairro','cep','id_cidade','id_uf')

    def get_queryset(self, request):
        queryset = super(EmpFilialAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset


class EquipamentoAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(EquipamentoAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset


class SalaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(SalaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

class ReservaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(ReservaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('id_usuario')
        return queryset

class HorarioAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(HorarioAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

admin.site.register(Cidade, cidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Departamentos, departamentoAdmin)
admin.site.register(EquipamentoMarca, EquipamentoMarcaAdmin)
admin.site.register(EquipamentoTipo, EquipamentoTipoAdmin)
admin.site.register(VeiculoCor, VeiculoCorAdmin)
admin.site.register(VeiculoMarca, VeiculoMarcaAdmin)
admin.site.register(VeiculoModelo, VeiculoModeloAdmin)
admin.site.register(VeiculoTipoCombustivel,VeiculoTipoCombustivelAdmin)
admin.site.register(VeiculoTipoVeiculo,VeiculoTipoVeiculoAdmin)
admin.site.register(EmpEmpresa, EmpEmpresaAdmin)
admin.site.register(EmpFilial, EmpFilialAdmin)
admin.site.register(Equipamento)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Veiculo)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Horario, HorarioAdmin)
