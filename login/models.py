from django.db import models


class Sesiones(models.Model):
    id_sesion = models.SmallAutoField(primary_key=True)
    usuario_ip = models.GenericIPAddressField()
    estado = models.CharField(max_length=100)
    datos_sesion = models.CharField(max_length=255)

    class Meta:
        db_table = 'eco_log_sesiones'
        verbose_name_plural = 'Datos de sesiones'

    def __str__(self):
        return str(self.id_sesion)
