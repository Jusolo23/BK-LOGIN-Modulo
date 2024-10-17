from django.db import models


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=170, null=False, blank=False)
    es_colombia = models.BooleanField(default=False)

    class Meta:
        db_table = 'eco_ext_pais'
        verbose_name_plural = 'Países'

    def __str__(self):
        return str(self.id_pais)


class Departamento(models.Model):
    id_departamento = models.IntegerField(primary_key=True)
    nombre_departamento = models.CharField(
        max_length=85, null=False, blank=False)
    pais = models.ForeignKey(Pais, to_field='id_pais',
                             on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_ext_departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return str(self.id_departamento)


class Municipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=85, null=False, blank=False)
    departamento = models.ForeignKey(
        Departamento, to_field='id_departamento', on_delete=models.CASCADE)

    class Meta:
        db_table = 'eco_ext_municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return str(self.id_municipio)


class ZonaUbicacion(models.Model):
    id_zubicacion = models.SmallAutoField(primary_key=True)
    nombre_zubicacion = models.CharField(max_length=10)

    class Meta:
        db_table = 'eco_bas_zonaubicacion'
        verbose_name_plural = 'Zona de ubicación'

    def __str__(self):
        return str(self.nombre_zubicacion)


class TipoIdentificacion(models.Model):
    id_tidentificacion = models.SmallAutoField(primary_key=True)
    nombre_tidentificacion = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipoidentificacion'
        verbose_name_plural = 'Tipo de identificación'

    def __str__(self):
        return str(self.nombre_tidentificacion)


class TipoGenero(models.Model):
    id_tgenero = models.SmallAutoField(primary_key=True)
    nombre_tgenero = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_tipogenero'
        verbose_name_plural = 'Tipo de género'

    def __str__(self):
        return str(self.nombre_tgenero)


class EstadoCivil(models.Model):
    id_ecivil = models.SmallAutoField(primary_key=True)
    nombre_ecivil = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_estadocivil'
        verbose_name_plural = 'Estado civil'

    def __str__(self):
        return str(self.nombre_ecivil)


class GpRh(models.Model):
    id_grh = models.SmallAutoField(primary_key=True)
    nombre_grh = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_gruporh'
        verbose_name_plural = 'Grupo rh'

    def __str__(self):
        return str(self.nombre_grh)


class FondoPensiones(models.Model):
    id_fpensiones = models.SmallAutoField(primary_key=True)
    nombre_fpensiones = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_fpensiones'
        verbose_name_plural = 'Fondo de pensiones'

    def __str__(self):
        return str(self.nombre_fpensiones)


class Eps(models.Model):
    id_eps = models.SmallAutoField(primary_key=True)
    nombre_eps = models.CharField(max_length=30)

    class Meta:
        db_table = 'eco_bas_eps'
        verbose_name_plural = 'Eps'

    def __str__(self):
        return str(self.nombre_eps)
