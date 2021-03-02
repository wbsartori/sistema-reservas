from django.db import models

# Create your models here.
class Equipamento(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)
    id_tipo_equipamento = models.ForeignKey('EquipamentoTipo', on_delete=models.CASCADE, db_column='id_tipo_equipamento', blank=True, null=True)
    id_equipamentos_marcas = models.ForeignKey('EquipamentoMarca', on_delete=models.CASCADE, db_column='id_equipamentos_marcas', blank=True, null=True)
    modelo = models.CharField(max_length=80, blank=True, null=True)
    numero_serie = models.CharField(max_length=50, blank=True, null=True)
    numero_patrimonio = models.CharField(max_length=20, blank=True, null=True)
    data_aquisicao = models.CharField(max_length=50, blank=True, null=True)
    nota_compra = models.CharField(max_length=50, blank=True, null=True)
    prazo_garantia_fabricante = models.CharField(max_length=50, blank=True, null=True)
    prazo_garantia_loja = models.CharField(max_length=50, blank=True, null=True)
    observacoes = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento'

    def __str__(self):
        return self.descricao

class EquipamentoMarca(models.Model):
    descricao = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento_marca'

    def __str__(self):
        return self.descricao

class EquipamentoTipo(models.Model):
    descricao = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento_tipo'

    def __str__(self):
        return self.descricao
