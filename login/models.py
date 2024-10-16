# from django.db import models
# from django.contrib.contenttypes.fields import GenericRelation
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User, Group


# class Sesiones(models.Model):
#     id_sesion = models.SmallAutoField(primary_key=True)
#     usuario = models.ForeignKey(
#         User, to_field='id', on_delete=models.CASCADE)
#     estado = models.BooleanField()
#     datos_sesion = models.CharField()
#     celular_dos = models.CharField(max_length=15, blank=True, null=True)
#     celular_emergencia = models.CharField(max_length=15, blank=True, null=True)

#     class Meta:
#         db_table = 'eco_con_ctelefono'
#         verbose_name_plural = 'Datos de contacto'

#     def __str__(self):
#         return str(self.id_ctelefono)
