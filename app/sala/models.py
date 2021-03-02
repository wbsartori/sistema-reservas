from django.db import models
from backend.models import EmpFilial, EmpEmpresa,Cidade,EmpDepartamento,Horario
from equipamento.models import Equipamento


class Sala(models.Model):
    id_empresa = models.ForeignKey('backend.EmpEmpresa', on_delete=models.CASCADE, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey('backend.EmpFilial', on_delete=models.CASCADE, db_column='id_filial', blank=True, null=True)
    descricao = models.CharField(max_length=80, blank=True, null=True)
    capacidade = models.IntegerField(blank=True, null=True)
    id_equipamentos = models.ForeignKey('equipamento.Equipamento', on_delete=models.CASCADE, db_column='id_equipamentos', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sala'

    def __str__(self):
        return self.descricao
