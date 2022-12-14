# Generated by Django 4.1 on 2022-11-30 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='asignaciones',
            fields=[
                ('container_tag_id', models.CharField(default='000000000000000000', max_length=21, primary_key=True, serialize=False, verbose_name='etiqueta')),
                ('user_audit_code', models.CharField(blank=True, max_length=10, null=True)),
                ('user_supervisor_code', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_asignacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Asignación')),
                ('container_stat_cd', models.IntegerField(default='15')),
                ('create_ts', models.DateTimeField(auto_now=True, verbose_name='Fecha Creación Etiqueta')),
            ],
            options={
                'verbose_name': 'asignacion',
                'verbose_name_plural': 'asignaciones',
                'db_table': 'asignaciones',
                'ordering': ['-fecha_asignacion'],
            },
        ),
        migrations.CreateModel(
            name='auditorias',
            fields=[
                ('container_tag_id', models.CharField(max_length=21, primary_key=True, serialize=False, verbose_name='Etiqueta DCL')),
                ('item_nbr', models.CharField(max_length=7)),
                ('user_audit_code', models.CharField(max_length=10)),
                ('fecha_asignacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Asignación')),
            ],
            options={
                'verbose_name': 'auditoria',
                'verbose_name_plural': 'auditorias',
                'db_table': 'auditorias',
                'ordering': ['-fecha_asignacion'],
            },
        ),
        migrations.CreateModel(
            name='auditorias_diarias_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=8, null=True)),
                ('container_tag_id', models.CharField(max_length=20, null=True, verbose_name='container_tag_id')),
                ('last_change_ts', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'auditoria diaria log',
                'verbose_name_plural': 'auditorias diarias log',
                'db_table': 'auditorias_diarias_log',
                'ordering': ['-last_change_ts'],
            },
        ),
        migrations.CreateModel(
            name='auditorias_diarias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_creacion_auditoria', models.DateTimeField(auto_now=True, null=True)),
                ('dc_nbr', models.CharField(max_length=10)),
                ('parent_container_tag_id', models.CharField(max_length=20)),
                ('container_id', models.CharField(max_length=10, verbose_name='container_id')),
                ('container_tag_id', models.CharField(max_length=20, verbose_name='container_tag_id')),
                ('container_stat_cd', models.IntegerField()),
                ('container_stat_dsc', models.CharField(max_length=25)),
                ('cntnr_type_code', models.IntegerField()),
                ('cntnr_type_desc', models.CharField(max_length=25)),
                ('parent_cntnr_id', models.CharField(max_length=8)),
                ('trip_create_date', models.DateTimeField()),
                ('label_format_code', models.IntegerField()),
                ('label_format_desc', models.CharField(max_length=45)),
                ('last_change_userid', models.CharField(max_length=10)),
                ('location_id', models.CharField(max_length=14)),
                ('dest_store_nbr', models.CharField(max_length=3)),
                ('dc_sel_section_id', models.CharField(max_length=6, null=True)),
                ('label_create_ts', models.DateTimeField()),
                ('item_nbr', models.CharField(max_length=6)),
                ('item1_desc', models.CharField(max_length=20)),
                ('dpto_name', models.CharField(max_length=30)),
                ('ship_unit_qty', models.IntegerField()),
                ('ship_unit_stat_cd', models.IntegerField()),
                ('shipunit_stat_desc', models.CharField(max_length=30)),
                ('cur_loc_slot_id', models.CharField(max_length=11)),
                ('last_change_ts', models.DateTimeField(auto_now=True)),
                ('create_ts', models.DateTimeField()),
                ('auditor_id', models.CharField(choices=[('j0c0af6', 'j0c0af6'), ('v0j0af6', 'v0j0af6'), ('C0j0a56', 'C0j0a56'), ('Z0j0a30', 'Z0j0a30')], default='No Asign', max_length=8, verbose_name='Auditor')),
                ('resolucion_cd', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Progreso', 'En Progreso'), ('Terminado', 'Terminado'), ('Cancelado', 'Cancelado')], default='Pendiente', max_length=13)),
                ('obs_auditoria_cd', models.CharField(default='Pendiente', max_length=30)),
                ('fecha_Asignacion', models.DateTimeField(auto_now=True, null=True)),
                ('supervisor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_creation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'auditoria diaria',
                'verbose_name_plural': 'auditorias diarias',
                'db_table': 'auditorias_diarias',
                'ordering': ['-create_ts'],
            },
        ),
    ]
