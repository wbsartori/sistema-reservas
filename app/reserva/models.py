from django.db import models
from backend.models import EmpFilial, EmpEmpresa,Cidade,EmpDepartamento,Horario
from sala.models import Sala
from equipamento.models import Equipamento, EquipamentoMarca, EquipamentoTipo
from veiculo.models import Veiculo,VeiculoTipoVeiculo,VeiculoMarca,VeiculoCor,VeiculoModelo,VeiculoTipoCombustivel

# Create your models here.
class Reserva(models.Model):
    TipoReserva_choices = (
        ("E", "Equipamento"),
        ("S", "Sala"),
        ("V", "Veiculo"),
        ("M", "Multiplos")
    )

    id_usuario = models.ForeignKey('backend.AuthUser', models.DO_NOTHING, db_column='id_usuario')
    data_inicio = models.DateField()
    data_final = models.DateField()
    id_horario = models.ForeignKey('backend.Horario', models.DO_NOTHING, db_column='id_horario')
    id_equipamento = models.ForeignKey('equipamento.Equipamento', models.DO_NOTHING, db_column='id_equipamento')
    id_sala = models.ForeignKey('sala.Sala', models.DO_NOTHING, db_column='id_sala')
    id_veiculo = models.ForeignKey('veiculo.Veiculo', models.DO_NOTHING, db_column='id_veiculo')
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    tipo_reserva = models.CharField(max_length=1, choices=TipoReserva_choices)

    class Meta:
        managed = False
        db_table = 'reserva'
