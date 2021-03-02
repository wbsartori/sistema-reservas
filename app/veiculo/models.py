from django.db import models
from backend.models import EmpFilial, EmpEmpresa,Cidade,EmpDepartamento,Horario

# Create your models.py.py here.
class Veiculo(models.Model):
    placa = models.CharField(max_length=10, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    renavam = models.CharField(max_length=20, blank=True, null=True)
    ano_fabricacao = models.CharField(max_length=12, blank=True, null=True)
    km_atual = models.IntegerField(blank=True, null=True)
    id_empresa = models.ForeignKey('backend.EmpEmpresa', on_delete=models.CASCADE, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey('backend.EmpFilial', on_delete=models.CASCADE, db_column='id_filial', blank=True, null=True)
    id_tipo_veiculo = models.ForeignKey('VeiculoTipoVeiculo', on_delete=models.CASCADE, db_column='id_tipo_veiculo', blank=True, null=True)
    id_combustivel = models.ForeignKey('VeiculoTipoCombustivel', on_delete=models.CASCADE, db_column='id_combustivel', blank=True, null=True)
    id_cores = models.ForeignKey('VeiculoCor', on_delete=models.CASCADE, db_column='id_cores', blank=True, null=True)
    id_marca = models.ForeignKey('VeiculoMarca', on_delete=models.CASCADE, db_column='id_marca', blank=True, null=True)
    id_modelo = models.ForeignKey('VeiculoModelo', on_delete=models.CASCADE, db_column='id_modelo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo'


class VeiculoCor(models.Model):
    descricao = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_cor'

    def __str__(self):
        return self.descricao


class VeiculoMarca(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_marca'

    def __str__(self):
        return self.descricao


class VeiculoModelo(models.Model):
    id_marca = models.ForeignKey(VeiculoMarca, on_delete=models.CASCADE, db_column='id_marca', blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_modelo'

    def __str__(self):
        return self.descricao

class VeiculoTipoCombustivel(models.Model):
    descricao = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_tipo_combustivel'

    def __str__(self):
        return self.descricao


class VeiculoTipoVeiculo(models.Model):
    descricao = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_tipo_veiculo'

    def __str__(self):
        return self.descricao
