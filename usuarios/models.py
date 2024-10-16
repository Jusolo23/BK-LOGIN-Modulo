from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User, Group

# DATOS CONTACTO


class TelefonoCelularContacto(models.Model):
    id_ctelefono = models.SmallAutoField(primary_key=True)
    celular_uno = models.CharField(max_length=15, blank=True, null=True)
    celular_dos = models.CharField(max_length=15, blank=True, null=True)
    celular_emergencia = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'eco_usr_ctelefono'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ctelefono)


class CorreoElectronicoContacto(models.Model):
    id_ccelectronico = models.SmallAutoField(primary_key=True)
    correo_electronico = models.EmailField(max_length=100)

    class Meta:
        db_table = 'eco_usr_ccelectronico'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_ccelectronico)


class DatosContacto(models.Model):
    id_contacto = models.SmallAutoField(primary_key=True)
    id_ctelefono = models.ForeignKey(
        TelefonoCelularContacto, to_field='id_ctelefono', on_delete=models.CASCADE)
    id_ccelectronico = models.ForeignKey(
        CorreoElectronicoContacto, to_field='id_ccelectronico', on_delete=models.CASCADE)
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'eco_usr_contacto'
        verbose_name_plural = 'Datos de contacto'

    def __str__(self):
        return str(self.id_contacto)

# DATOS UBICACION


# class Pais(models.Model):
#     id_pais = models.AutoField(primary_key=True)
#     nombre_pais = models.CharField(max_length=170, null=False, blank=False)
#     es_colombia = models.BooleanField(default=False)

#     class Meta:
#         db_table = 'eco_usr_pais'
#         verbose_name_plural = 'Países'

#     def __str__(self):
#         return str(self.id_pais)


# class Departamento(models.Model):
#     id_departamento = models.IntegerField(primary_key=True)
#     nombre_departamento = models.CharField(
#         max_length=85, null=False, blank=False)
#     pais = models.ForeignKey(Pais, to_field='id_pais',
#                              on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'eco_usr_departamento'
#         verbose_name_plural = 'Departamentos'

#     def __str__(self):
#         return str(self.id_departamento)


# class Municipio(models.Model):
#     id_municipio = models.IntegerField(primary_key=True)
#     nombre_municipio = models.CharField(max_length=85, null=False, blank=False)
#     departamento = models.ForeignKey(
#         Departamento, to_field='id_departamento', on_delete=models.CASCADE)

#     class Meta:
#         db_table = 'eco_usr_municipio'
#         verbose_name_plural = 'Municipios'

#     def __str__(self):
#         return str(self.id_municipio)


# class ZonaUbicacion(models.Model):
#     id_zubicacion = models.SmallAutoField(primary_key=True)
#     nombre_zubicacion = models.CharField(max_length=10)

#     class Meta:
#         db_table = 'eco_usr_zonaubicacion'
#         verbose_name_plural = 'Zona de ubicación'

#     def __str__(self):
#         return str(self.nombre_zubicacion)


class DatosUbicacion(models.Model):
    id_ubicacion = models.AutoField(primary_key=True)
    pais = models.ForeignKey(Pais, to_field='id_pais',
                             on_delete=models.CASCADE)
    departamento = models.ForeignKey(
        Departamento, to_field='id_departamento', on_delete=models.CASCADE)
    municipio = models.ForeignKey(
        Municipio, to_field='id_municipio', on_delete=models.CASCADE)
    zona = models.ForeignKey(
        ZonaUbicacion, to_field='id_zubicacion', on_delete=models.CASCADE)
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


class UbicacionRural(DatosUbicacion):
    corregimiento = models.CharField(max_length=150, null=True, blank=True)
    centro_poblado = models.CharField(max_length=150, null=True, blank=True)
    vereda = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.direccion

    class Meta:
        db_table = 'eco_usr_direccionrural'
        verbose_name_plural = 'Dirección rural'


class direccionUrbana(DatosUbicacion):
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


# class TipoIdentificacion(models.Model):
#     id_tidentificacion = models.SmallAutoField(primary_key=True)
#     nombre_tidentificacion = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_tipoidentificacion'
#         verbose_name_plural = 'Tipo de identificación'

#     def __str__(self):
#         return str(self.nombre_tidentificacion)


class IdentificacionUsuario(models.Model):
    id_iusuario = models.AutoField(primary_key=True)
    numero_identificacion = models.CharField(
        max_length=20, null=False, blank=True)
    fecha_expedicion = models.DateField()
    tipo_identificacion = models.ForeignKey(
        TipoIdentificacion, to_field='id_tidentificacion', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_usr_iusuario'
        verbose_name_plural = 'Datos de la identificación del usuario'

    def __str__(self):
        return str(self.numero_identificacion) + str(self.fecha_expedicion)


# class TipoGenero(models.Model):
#     id_tgenero = models.SmallAutoField(primary_key=True)
#     nombre_tgenero = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_tipogenero'
#         verbose_name_plural = 'Tipo de género'

#     def __str__(self):
#         return str(self.nombre_tgenero)


# class EstadoCivil(models.Model):
#     id_ecivil = models.SmallAutoField(primary_key=True)
#     nombre_ecivil = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_estadocivil'
#         verbose_name_plural = 'Estado civil'

#     def __str__(self):
#         return str(self.nombre_ecivil)


# class GpRh(models.Model):
#     id_grh = models.SmallAutoField(primary_key=True)
#     nombre_grh = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_gruporh'
#         verbose_name_plural = 'Grupo rh'

#     def __str__(self):
#         return str(self.nombre_grh)


# class FondoPensiones(models.Model):
#     id_fpensiones = models.SmallAutoField(primary_key=True)
#     nombre_fpensiones = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_fpensiones'
#         verbose_name_plural = 'Fondo de pensiones'

#     def __str__(self):
#         return str(self.nombre_fpensiones)


# class Eps(models.Model):
#     id_eps = models.SmallAutoField(primary_key=True)
#     nombre_eps = models.CharField(max_length=30)

#     class Meta:
#         db_table = 'eco_usr_eps'
#         verbose_name_plural = 'Eps'

#     def __str__(self):
#         return str(self.nombre_eps)


class Dependencia(models.Model):
    id_dependencia = models.SmallAutoField(primary_key=True)
    nombre_dependencia = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_usr_dependencia'
        verbose_name_plural = 'Dependencia'

    def __str__(self):
        return str(self.nombre_dependencia)
    
class Grupo(models.Model):
    id_grupo = models.SmallAutoField(primary_key=True)
    nombre_grupo = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_usr_grupo'
        verbose_name_plural = 'Grupo'

    def __str__(self):
        return str(self.nombre_grupo)

class Rol(models.Model):
    id_rol = models.SmallAutoField(primary_key=True)
    nombre_rol = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_usr_rol'
        verbose_name_plural = 'Rol'

    def __str__(self):
        return str(self.nombre_rol)

class DatosBasicosUsuario(models.Model):
    id_busuario = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(
        User, to_field='id', on_delete=models.CASCADE)
    identificacion_usuario = models.ForeignKey(
        IdentificacionUsuario, to_field='id_iusuario', on_delete=models.CASCADE)
    genero_persona = models.ForeignKey(
        TipoGenero, to_field='id_tgenero', on_delete=models.CASCADE, null=True)
    estado_civil = models.ForeignKey(
        EstadoCivil, to_field='id_ecivil', on_delete=models.CASCADE, null=True)
    gp_rh = models.ForeignKey(GpRh, to_field='id_grh',
                              on_delete=models.CASCADE, null=True)
    fondo_pensiones = models.ForeignKey(FondoPensiones, to_field='id_fpensiones',
                                        on_delete=models.CASCADE, null=True)
    eps = models.ForeignKey(Eps, to_field='id_eps',
                            on_delete=models.CASCADE, null=True)
    ubicacion_persona = GenericRelation(DatosUbicacion)
    contacto_persona = GenericRelation(DatosContacto)
    contrato = models.IntegerField()
    dependencia = models.ForeignKey(
        Dependencia, to_field='id_dependencia', on_delete=models.CASCADE)
    grupo = models.ForeignKey(
        Grupo, to_field='id_grupo', on_delete=models.CASCADE)
    rol = models.ForeignKey(
        Rol, to_field='id_rol', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_usr_basicosusuario'
        verbose_name_plural = 'Datos básicos del usuario'

    def __str__(self):
        return str(self.id_busuario)
