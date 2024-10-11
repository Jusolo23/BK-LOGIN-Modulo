# Generated by Django 5.1.2 on 2024-10-09 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CorreoElectronicoContacto',
            fields=[
                ('id_ccelectronico', models.SmallAutoField(primary_key=True, serialize=False)),
                ('correo_electronico', models.EmailField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_con_ccelectronico',
            },
        ),
        migrations.CreateModel(
            name='DatosUbicacion',
            fields=[
                ('id_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=160, null=True)),
                ('indicacion', models.CharField(blank=True, max_length=160, null=True)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name_plural': 'Datos de ubicación',
                'db_table': 'eco_ubi_ubicacion',
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id_departamento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_departamento', models.CharField(max_length=85)),
            ],
            options={
                'verbose_name_plural': 'Departamentos',
                'db_table': 'eco_ubi_departamento',
            },
        ),
        migrations.CreateModel(
            name='Dependencia',
            fields=[
                ('id_dependencia', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_dependencia', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Dependencia',
                'db_table': 'eco_bas_dependencia',
            },
        ),
        migrations.CreateModel(
            name='Eps',
            fields=[
                ('id_eps', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_eps', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Eps',
                'db_table': 'eco_bas_eps',
            },
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id_ecivil', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_ecivil', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Estado civil',
                'db_table': 'eco_bas_estadocivil',
            },
        ),
        migrations.CreateModel(
            name='FondoPensiones',
            fields=[
                ('id_fpensiones', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_fpensiones', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Fondo de pensiones',
                'db_table': 'eco_bas_fpensiones',
            },
        ),
        migrations.CreateModel(
            name='GpRh',
            fields=[
                ('id_grh', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_grh', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Grupo rh',
                'db_table': 'eco_bas_gruporh',
            },
        ),
        migrations.CreateModel(
            name='IdentificacionUsuario',
            fields=[
                ('id_iusuario', models.AutoField(primary_key=True, serialize=False)),
                ('numero_identificacion', models.CharField(blank=True, max_length=20)),
                ('fecha_expedicion', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Datos de la identificación del usuario',
                'db_table': 'eco_bas_iusuario',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_pais', models.CharField(max_length=170)),
                ('es_colombia', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Países',
                'db_table': 'eco_ubi_pais',
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Rol',
                'db_table': 'eco_bas_rol',
            },
        ),
        migrations.CreateModel(
            name='TelefonoCelularContacto',
            fields=[
                ('id_ctelefono', models.SmallAutoField(primary_key=True, serialize=False)),
                ('celular_uno', models.CharField(blank=True, max_length=15, null=True)),
                ('celular_dos', models.CharField(blank=True, max_length=15, null=True)),
                ('celular_emergencia', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_con_ctelefono',
            },
        ),
        migrations.CreateModel(
            name='TipoGenero',
            fields=[
                ('id_tgenero', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_tgenero', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tipo de género',
                'db_table': 'eco_bas_tipogenero',
            },
        ),
        migrations.CreateModel(
            name='TipoIdentificacion',
            fields=[
                ('id_tidentificacion', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_tidentificacion', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Tipo de identificación',
                'db_table': 'eco_bas_tipoidentificacion',
            },
        ),
        migrations.CreateModel(
            name='ZonaUbicacion',
            fields=[
                ('id_zubicacion', models.SmallAutoField(primary_key=True, serialize=False)),
                ('nombre_zubicacion', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Zona de ubicación',
                'db_table': 'eco_ubi_zonaubicacion',
            },
        ),
        migrations.CreateModel(
            name='direccionUrbana',
            fields=[
                ('datosubicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.datosubicacion')),
                ('nombre_barrio', models.CharField(blank=True, max_length=100, null=True)),
                ('tipo_viaprincipal', models.CharField(blank=True, max_length=20, null=True)),
                ('numero_viaprincipal', models.IntegerField(blank=True, null=True)),
                ('letra_principal', models.CharField(blank=True, max_length=10, null=True)),
                ('es_bis', models.BooleanField(null=True)),
                ('cuadrante_principal', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_viasecundaria', models.IntegerField(blank=True, null=True)),
                ('letra_secundaria', models.CharField(blank=True, max_length=10, null=True)),
                ('cuadrante_secundario', models.CharField(blank=True, max_length=10, null=True)),
                ('numero_placa', models.IntegerField(blank=True, null=True)),
                ('complemento', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'verbose_name_plural': 'Dirección urbana',
                'db_table': 'eco_ubi_direccionurbana',
            },
            bases=('login.datosubicacion',),
        ),
        migrations.CreateModel(
            name='UbicacionRural',
            fields=[
                ('datosubicacion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='login.datosubicacion')),
                ('corregimiento', models.CharField(blank=True, max_length=150, null=True)),
                ('centro_poblado', models.CharField(blank=True, max_length=150, null=True)),
                ('vereda', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Dirección rural',
                'db_table': 'eco_ubi_direccionrural',
            },
            bases=('login.datosubicacion',),
        ),
        migrations.AddField(
            model_name='datosubicacion',
            name='departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.departamento'),
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id_municipio', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_municipio', models.CharField(max_length=85)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.departamento')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'db_table': 'eco_ubi_municipio',
            },
        ),
        migrations.AddField(
            model_name='datosubicacion',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.municipio'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.pais'),
        ),
        migrations.AddField(
            model_name='datosubicacion',
            name='pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.pais'),
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id_sesion', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=200)),
                ('fecha_entrada', models.DateTimeField()),
                ('fecha_salida', models.DateTimeField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Datos de las sesiones',
                'db_table': 'eco_sis_sesion',
            },
        ),
        migrations.CreateModel(
            name='DatosContacto',
            fields=[
                ('id_contacto', models.SmallAutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('id_ccelectronico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.correoelectronicocontacto')),
                ('id_ctelefono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.telefonocelularcontacto')),
            ],
            options={
                'verbose_name_plural': 'Datos de contacto',
                'db_table': 'eco_con_contacto',
            },
        ),
        migrations.CreateModel(
            name='DatosBasicosUsuario',
            fields=[
                ('id_busuario', models.AutoField(primary_key=True, serialize=False)),
                ('contrato', models.IntegerField()),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dependencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.dependencia')),
                ('eps', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.eps')),
                ('estado_civil', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.estadocivil')),
                ('fondo_pensiones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.fondopensiones')),
                ('gp_rh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.gprh')),
                ('identificacion_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.identificacionusuario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.rol')),
                ('genero_persona', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.tipogenero')),
            ],
            options={
                'verbose_name_plural': 'Datos básicos del usuario',
                'db_table': 'eco_bas_basicosusuario',
            },
        ),
        migrations.AddField(
            model_name='identificacionusuario',
            name='tipo_identificacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.tipoidentificacion'),
        ),
        migrations.AddField(
            model_name='datosubicacion',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.zonaubicacion'),
        ),
    ]
