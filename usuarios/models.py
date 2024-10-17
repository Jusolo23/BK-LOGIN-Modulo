from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from sistema import models as sis_models


# DATOS CONTACTO

class TelefonoCelularContactoUsuario(models.Model):
    id_ctelefono = models.SmallAutoField(primary_key=True)
    celular_uno = models.CharField(max_length=15, blank=True, null=True)
    celular_dos = models.CharField(max_length=15, blank=True, null=True)
    celular_emergencia = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'eco_usr_ctelefono'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ctelefono)


class CorreoElectronicoContactoUsuario(models.Model):
    id_ccelectronico = models.SmallAutoField(primary_key=True)
    correo_electronico = models.EmailField(max_length=100)

    class Meta:
        db_table = 'eco_usr_ccelectronico'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ccelectronico)


class DatosContactoUsuario(models.Model):
    id_contacto = models.SmallAutoField(primary_key=True)
    id_ctelefono = models.ForeignKey(
        TelefonoCelularContactoUsuario, to_field='id_ctelefono', on_delete=models.CASCADE)
    id_ccelectronico = models.ForeignKey(
        CorreoElectronicoContactoUsuario, to_field='id_ccelectronico', on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_usr_contacto'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_contacto)


# DATOS UBICACION

class DatosUbicacionUsuario(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    pais = models.ForeignKey(
        sis_models.Pais, to_field='id_pais', on_delete=models.CASCADE)
    departamento = models.ForeignKey(
        sis_models.Departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        sis_models.Municipio, to_field='id_municipio', on_delete=models.CASCADE)
    zona = models.ForeignKey(sis_models.ZonaUbicacion,
                             to_field='id_zubicacion', on_delete=models.CASCADE)
    direccion = models.CharField(max_length=160, blank=True, null=True)
    indicacion = models.CharField(max_length=160, blank=True, null=True)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_usr_ubicacion'
        verbose_name_plural = 'Datos de ubicación'

    def __str__(self):
        return str(self.id_ubicacion)


class UbicacionRural(DatosUbicacionUsuario):
    corregimiento = models.CharField(max_length=150, null=True, blank=True)
    centro_poblado = models.CharField(max_length=150, null=True, blank=True)
    vereda = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'eco_usr_direccionrural'
        verbose_name_plural = 'Dirección rural'


class direccionUrbana(DatosUbicacionUsuario):
    nombre_barrio = models.CharField(max_length=100, null=True, blank=True)
    tipo_viaprincipal = models.CharField(max_length=20, null=True, blank=True)
    numero_viaprincipal = models.IntegerField(null=True, blank=True)
    letra_principal = models.CharField(max_length=10, null=True, blank=True)
    es_bis = models.BooleanField(null=True)
    cuadrante_principal = models.CharField(
        max_length=10, null=True, blank=True)
    numero_viasecundaria = models.IntegerField(null=True, blank=True)
    letra_secundaria = models.CharField(max_length=10, null=True, blank=True)
    cuadrante_secundario = models.CharField(
        max_length=10, null=True, blank=True)
    numero_placa = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        fields = [
            self.tipo_viaprincipal, self.numero_viaprincipal, self.letra_principal,
            self.cuadrante_principal, self.numero_viasecundaria, self.letra_secundaria, self.numero_placa,
            self.cuadrante_secundario, self.complemento]

        fields = [str(field) for field in fields if field]
        return " ".join(fields)

    class Meta:
        db_table = 'eco_usr_direccionurbana'
        verbose_name_plural = 'Dirección urbana'


# DATOS BASICOS

class IdentificacionUsuario(models.Model):
    id_iusuario = models.AutoField(primary_key=True)
    numero_identificacion = models.CharField(
        max_length=20, null=False, blank=True)
    fecha_expedicion = models.DateField()
    tipo_identificacion = models.ForeignKey(
        sis_models.TipoIdentificacion, to_field='id_tidentificacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_usr_iusuario'
        verbose_name_plural = 'Datos de la identificación del usuario'

    def __str__(self):
        return str(self.numero_identificacion) + str(self.fecha_expedicion)


class NombrePersonaUsuario(models.Model):
    id_npersona = models.AutoField(primary_key=True)
    primer_nombre = models.CharField(max_length=20, null=False, blank=False)
    segundo_nombre = models.CharField(max_length=50, null=True, blank=True)
    primer_apellido = models.CharField(max_length=50, null=False, blank=False)
    segundo_apellido = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'eco_usr_nombrepersona'
        verbose_name_plural = 'Nombres y apellidos de las personas'

    def __str__(self):
        return str(self.id_npersona) + str(self.primer_nombre)


class DatosBasicosUsuario(models.Model):
    id_busuario = models.AutoField(primary_key=True)
    identificacion_usuario = models.ForeignKey(
        IdentificacionUsuario, to_field='id_iusuario', on_delete=models.CASCADE)
    nombre_persona = models.ForeignKey(
        NombrePersonaUsuario, to_field='id_npersona',  on_delete=models.CASCADE)
    genero_persona = models.ForeignKey(
        sis_models.TipoGenero, to_field='id_tgenero', on_delete=models.CASCADE, null=True)
    gp_rh = models.ForeignKey(
        sis_models.GpRh, to_field='id_grh', on_delete=models.CASCADE, null=True)
    ubicacion_persona = GenericRelation(DatosUbicacionUsuario)
    contacto_persona = GenericRelation(DatosContactoUsuario)

    class Meta:
        db_table = 'eco_usr_basicosusuario'
        verbose_name_plural = 'Datos básicos del usuario'

    def __str__(self):
        return str(self.id_busuario)


# DATOS COMPLEMENTARIOS

class TipoVinculacion(models.Model):
    id_tvinculacion = models.AutoField(primary_key=True)
    nombre_tvinculacion = models.CharField(
        max_length=30, null=True, blank=True)

    class Meta:
        db_table = 'eco_bas_tipovinculacion'
        verbose_name_plural = 'Tipo de vinculación a la UNP'

    def __str__(self):
        return str(self.id_busuario)


class DatosComplementariosUsuario(models.Model):
    id_cusuario = models.AutoField(primary_key=True)
    estado_civil = models.ForeignKey(
        sis_models.EstadoCivil, to_field='id_ecivil', on_delete=models.CASCADE, null=True)
    fondo_pensiones = models.ForeignKey(
        sis_models.FondoPensiones, to_field='id_fpensiones', on_delete=models.CASCADE, null=True)
    eps = models.ForeignKey(sis_models.Eps, to_field='id_eps',
                            on_delete=models.CASCADE, null=True)
    tipo_vinculacion = models.ForeignKey(
        TipoVinculacion, to_field='id_tvinculacion', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'eco_usr_complementariosusuario'
        verbose_name_plural = 'Datos básicos del usuario'

    def __str__(self):
        return str(self.id_cusuario)


class ContratoContratista(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    numero_contrato = models.CharField(max_length=10, blank=True, null=True)
    fecha_iniciocontrato = models.DateField(blank=True, null=True)
    fecha_fincontrato = models.DateField(blank=True, null=True)
    datos_complementarios = GenericRelation(DatosComplementariosUsuario)

    class Meta:
        db_table = 'eco_usr_datoscontrato'
        verbose_name_plural = 'Datos básicos del contrato'

    def __str__(self):
        return str(self.id_contrato)


class ResolucionFuncionario(models.Model):
    id_resolucion = models.AutoField(primary_key=True)
    numero_resolucion = models.CharField(max_length=30, blank=True, null=True)
    datos_complementarios = GenericRelation(DatosComplementariosUsuario)

    class Meta:
        db_table = 'eco_usr_datosresolucion'
        verbose_name_plural = 'Datos básicos de la resolucion del contratista'

    def __str__(self):
        return str(self.id_resolucion)


# DATOS PARA DEFINIR EL PERFIL DE USUARIO

class Dependencia(models.Model):
    id_dependencia = models.SmallAutoField(primary_key=True)
    nombre_dependencia = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_dependencia'
        verbose_name_plural = 'Dependencia'

    def __str__(self):
        return str(self.nombre_dependencia)


class Grupo(models.Model):
    id_grupo = models.SmallAutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_grupo'
        verbose_name_plural = 'Grupo'

    def __str__(self):
        return str(self.nombre_grupo)


class Rol(models.Model):
    id_rol = models.SmallAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_rol'
        verbose_name_plural = 'Rol'

    def __str__(self):
        return str(self.nombre_rol)


class PerfilUsuario(models.Model):
    id_pusuario = models.AutoField(primary_key=True)
    dependencia = models.ForeignKey(
        Dependencia, to_field='id_dependencia', on_delete=models.CASCADE)
    grupo = models.ForeignKey(
        Grupo, to_field='id_grupo', on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, to_field='id_rol', on_delete=models.CASCADE)
    acepto_politicas = models.BooleanField(default=False)
    datos_basicos = GenericRelation(DatosBasicosUsuario)

    class Meta:
        db_table = 'eco_usr_perfilusuario'
        verbose_name_plural = 'perfil del usuario'

    def __str__(self):
        return str(self.id_pusuario)
