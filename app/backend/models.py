from django.db import models
from datetime import datetime

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE)
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
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE)

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


class Cidade(models.Model):
    codigo_ibge = models.CharField(max_length=7, blank=True, null=True)
    id_uf = models.ForeignKey('Estado', on_delete=models.CASCADE, db_column='id_uf', blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cidade'

    def __str__(self):
        return self.cidade


class Departamentos(models.Model):
    descricao = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamentos'

    def __str__(self):
        return self.descricao


class EmpDepartamento(models.Model):
    id_departamento = models.ForeignKey('Departamentos', on_delete=models.CASCADE, db_column='id_departamento', blank=True, null=True)
    id_empresa = models.ForeignKey('EmpEmpresa', on_delete=models.CASCADE, db_column='id_empresa', blank=True, null=True)
    id_filial = models.ForeignKey('EmpFilial', on_delete=models.CASCADE, db_column='id_filial', blank=True, null=True)

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
    cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, blank=True, null=True)
    uf = models.ForeignKey('Estado', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_empresa'

    def __str__(self):
        return self.descricao

class EmpFilial(models.Model):
    id_empresa = models.ForeignKey('EmpEmpresa', on_delete=models.CASCADE, db_column='id_empresa', blank=True, null=True)
    codigo = models.CharField(max_length=12, blank=True, null=True)
    descricao = models.CharField(max_length=80, blank=True, null=True)
    endereco = models.CharField(max_length=80, blank=True, null=True)
    complemento = models.CharField(max_length=40, blank=True, null=True)
    numero = models.CharField(max_length=10, blank=True, null=True)
    bairro = models.CharField(max_length=50, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    id_cidade = models.ForeignKey('Cidade', on_delete=models.CASCADE, db_column='id_cidade', blank=True, null=True)
    id_uf = models.ForeignKey('Estado', on_delete=models.CASCADE, db_column='id_uf', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emp_filial'

    def __str__(self):
        return self.descricao


class Estado(models.Model):
    descricao = models.CharField(max_length=50, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'

    def __str__(self):
        return self.descricao


class Horario(models.Model):
    descricao = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'horario'

    def __str__(self):
        return self.descricao


