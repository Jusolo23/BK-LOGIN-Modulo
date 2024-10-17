# Generated by Django 5.1.2 on 2024-10-17 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0002_remove_datoscontacto_id_ccelectronico_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sesiones',
            fields=[
                ('id_sesion', models.SmallAutoField(primary_key=True, serialize=False)),
                ('usuario_ip', models.GenericIPAddressField()),
                ('estado', models.CharField(max_length=100)),
                ('datos_sesion', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Datos de sesiones',
                'db_table': 'eco_log_sesiones',
            },
        ),
    ]
