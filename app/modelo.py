# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cidade(models.Model):
    codigo_ibge = models.CharField(max_length=7, blank=True, null=True)
    id_uf = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_uf', blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cidade'


class Departamentos(models.Model):
    descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmpDepartamento(models.Model):
    id_departamento = models.ForeignKey('self', models.DO_NOTHING, db_column='id_departamento', blank=True, null=True)
    id_empresa = models.ForeignKey('EmpEmpresa', models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey('EmpFilial', models.DO_NOTHING, db_column='id_filial', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_departamento'


class EmpEmpresa(models.Model):
    codigo = models.CharField(max_length=12, blank=True, null=True)
    descricao = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    complemento = models.CharField(max_length=40, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    cidade = models.ForeignKey(Cidade, models.DO_NOTHING, blank=True, null=True)
    uf = models.ForeignKey('Estado', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_empresa'


class EmpFilial(models.Model):
    id_empresa = models.ForeignKey(EmpEmpresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    codigo = models.CharField(max_length=12, blank=True, null=True)
    descricao = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    complemento = models.CharField(max_length=40, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    id_cidade = models.ForeignKey(Cidade, models.DO_NOTHING, db_column='id_cidade', blank=True, null=True)
    id_uf = models.ForeignKey('Estado', models.DO_NOTHING, db_column='id_uf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_filial'


class Equipamento(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)
    id_tipo_equipamento = models.ForeignKey('EquipamentoTipo', models.DO_NOTHING, db_column='id_tipo_equipamento', blank=True, null=True)
    id_equipamentos_marcas = models.ForeignKey('EquipamentoMarca', models.DO_NOTHING, db_column='id_equipamentos_marcas', blank=True, null=True)
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


class EquipamentoMarca(models.Model):
    descricao = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento_marca'


class EquipamentoTipo(models.Model):
    descricao = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipamento_tipo'


class Estado(models.Model):
    descricao = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class Horario(models.Model):
    descricao = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'


class Reserva(models.Model):
    id_usuario = models.ForeignKey(AuthUser, models.DO_NOTHING, db_column='id_usuario')
    data_inicio = models.DateField()
    data_final = models.DateField()
    hora_inicial = models.ForeignKey(Horario, models.DO_NOTHING, db_column='hora_inicial')
    hora_final = models.ForeignKey(Horario, models.DO_NOTHING, db_column='hora_final')
    id_equipamento = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='id_equipamento', blank=True, null=True)
    id_sala = models.ForeignKey('Sala', models.DO_NOTHING, db_column='id_sala', blank=True, null=True)
    id_veiculo = models.ForeignKey('Veiculo', models.DO_NOTHING, db_column='id_veiculo', blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reserva'


class Sala(models.Model):
    id_empresa = models.ForeignKey(EmpEmpresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey(EmpFilial, models.DO_NOTHING, db_column='id_filial', blank=True, null=True)
    descricao = models.CharField(max_length=80, blank=True, null=True)
    capacidade = models.IntegerField(blank=True, null=True)
    id_equipamentos = models.ForeignKey(Equipamento, models.DO_NOTHING, db_column='id_equipamentos', blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sala'


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    renavam = models.CharField(max_length=20, blank=True, null=True)
    ano_fabricacao = models.CharField(max_length=12, blank=True, null=True)
    km_atual = models.IntegerField(blank=True, null=True)
    km_anterior = models.IntegerField(blank=True, null=True)
    id_empresa = models.ForeignKey(EmpEmpresa, models.DO_NOTHING, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey(EmpFilial, models.DO_NOTHING, db_column='id_filial', blank=True, null=True)
    id_tipo_veiculo = models.ForeignKey('VeiculoTipoVeiculo', models.DO_NOTHING, db_column='id_tipo_veiculo', blank=True, null=True)
    id_combustivel = models.ForeignKey('VeiculoTipoCombustivel', models.DO_NOTHING, db_column='id_combustivel', blank=True, null=True)
    id_cores = models.ForeignKey('VeiculoCor', models.DO_NOTHING, db_column='id_cores', blank=True, null=True)
    id_marca = models.ForeignKey('VeiculoMarca', models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    id_modelo = models.ForeignKey('VeiculoModelo', models.DO_NOTHING, db_column='id_modelo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo'


class VeiculoCor(models.Model):
    descricao = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_cor'


class VeiculoMarca(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_marca'


class VeiculoModelo(models.Model):
    id_marca = models.ForeignKey(VeiculoMarca, models.DO_NOTHING, db_column='id_marca', blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_modelo'


class VeiculoTipoCombustivel(models.Model):
    descricao = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_tipo_combustivel'


class VeiculoTipoVeiculo(models.Model):
    descricao = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'veiculo_tipo_veiculo'