# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BolFac(models.Model):
    id_bol_fac = models.FloatField(primary_key=True)
    precio = models.FloatField(blank=True, null=True)
    res_hora_id_hora = models.ForeignKey('ResHora', models.DO_NOTHING, db_column='res_hora_id_hora')
    cliente_rut = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='cliente_rut')

    class Meta:
        managed = False
        db_table = 'bol_fac'


class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    patente = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'cliente'


class DetalleProducto(models.Model):
    id_hora = models.FloatField()
    id_producto = models.FloatField()
    precio = models.FloatField()
    cantidad = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detalle_producto'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    rut_empleado = models.FloatField(primary_key=True)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    usuario = models.CharField(max_length=25)
    contrasenia = models.CharField(max_length=25)
    tipo_empleado_id_tipo_empleado = models.ForeignKey('TipoEmpleado', models.DO_NOTHING, db_column='tipo_empleado_id_tipo_empleado')

    class Meta:
        managed = False
        db_table = 'empleado'


class OrdPedido(models.Model):
    id_orden = models.FloatField(primary_key=True)
    fecha_orden = models.DateField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    precio = models.FloatField()
    cantidad = models.FloatField()
    id_producto = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ord_pedido'


class ProdProv(models.Model):
    id_producto = models.FloatField(primary_key=True)
    fam_prod = models.CharField(max_length=20)
    fec_venc = models.DateField()
    precio = models.FloatField()
    stock = models.FloatField()

    class Meta:
        managed = False
        db_table = 'prod_prov'


class ProdProvProveedor(models.Model):
    prod_prov_id_producto = models.OneToOneField(ProdProv, models.DO_NOTHING, db_column='prod_prov_id_producto', primary_key=True)
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')

    class Meta:
        managed = False
        db_table = 'prod_prov_proveedor'
        unique_together = (('prod_prov_id_producto', 'proveedor_id_proveedor'),)


class ProdServ(models.Model):
    id_producto = models.FloatField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()
    stock = models.FloatField()
    stock_critico = models.FloatField()
    codificacion = models.FloatField()
    empleado_rut_empleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_rut_empleado')

    class Meta:
        managed = False
        db_table = 'prod_serv'


class Proveedor(models.Model):
    id_proveedor = models.FloatField(primary_key=True)
    telefono = models.FloatField()
    direccion = models.CharField(max_length=20)
    rubro = models.CharField(max_length=20)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'proveedor'


class ResHora(models.Model):
    id_hora = models.FloatField(primary_key=True)
    detalle = models.CharField(max_length=50)
    fecha = models.DateField()
    mecanico = models.CharField(max_length=25, blank=True, null=True)
    estado = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'res_hora'


class ResHoraEmpleado(models.Model):
    id_empleado = models.FloatField()
    id_hora = models.FloatField()

    class Meta:
        managed = False
        db_table = 'res_hora_empleado'


class ResHoraEmpleadoFk(models.Model):
    id_empleado = models.OneToOneField(Empleado, models.DO_NOTHING, db_column='id_empleado', primary_key=True)
    id_hora = models.ForeignKey(ResHora, models.DO_NOTHING, db_column='id_hora')

    class Meta:
        managed = False
        db_table = 'res_hora_empleado_fk'
        unique_together = (('id_empleado', 'id_hora'),)


class Servicio(models.Model):
    id_servicio = models.FloatField(primary_key=True)
    tipo_servicio = models.CharField(max_length=20)
    res_hora_id_hora = models.ForeignKey(ResHora, models.DO_NOTHING, db_column='res_hora_id_hora')

    class Meta:
        managed = False
        db_table = 'servicio'


class TipoEmpleado(models.Model):
    id_tipo_empleado = models.FloatField(primary_key=True)
    tipo_empleado = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tipo_empleado'
