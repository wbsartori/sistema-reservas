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


class HorarioAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(HorarioAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

admin.site.register(Cidade, cidadeAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(Departamentos, departamentoAdmin)
admin.site.register(EmpEmpresa, EmpEmpresaAdmin)
admin.site.register(EmpFilial, EmpFilialAdmin)
admin.site.register(Horario, HorarioAdmin)
