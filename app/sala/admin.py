from django.contrib import admin
from .models import *

# Register your models here.
class SalaAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(SalaAdmin, self).get_queryset(request)
        queryset = queryset.order_by('descricao')
        return queryset

admin.site.register(Sala, SalaAdmin)