# Generated by Django 4.1 on 2022-09-12 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asignaciones',
            fields=[
                ('etiqueta', models.CharField(max_length=21, primary_key=True, serialize=False)),
                ('user_audit_code', models.CharField(blank=True, max_length=10, null=True)),
                ('user_supervisor_code', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha_asignacion', models.DateTimeField(auto_now=True, verbose_name='Fecha Asignación')),
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
                ('etiqueta', models.CharField(max_length=21, primary_key=True, serialize=False, verbose_name='Etiqueta DCL')),
                ('item_nbr', models.CharField(max_length=7)),
                ('user_audit_code', models.CharField(max_length=10)),
                ('fecha_asignacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'auditoria',
                'verbose_name_plural': 'auditorias',
                'db_table': 'auditorias',
                'ordering': ['-fecha_asignacion'],
            },
        ),
        migrations.CreateModel(
            name='auditorias_diarias',
            fields=[
                ('dc_nbr', models.IntegerField()),
                ('user', models.CharField(blank=True, max_length=8, null=True, verbose_name='Auditor')),
                ('container_id', models.CharField(max_length=9)),
                ('parent_container_tag_id', models.CharField(max_length=20)),
                ('container_tag_id', models.CharField(max_length=20)),
                ('container_stat_cd', models.IntegerField()),
                ('container_stat_dsc', models.CharField(max_length=25)),
                ('cntnr_type_code', models.IntegerField()),
                ('cntnr_type_desc', models.CharField(max_length=25)),
                ('parent_cntnr_id', models.CharField(max_length=8)),
                ('trip_create_date', models.DateTimeField()),
                ('label_format_code', models.IntegerField()),
                ('label_format_desc', models.CharField(max_length=45)),
                ('location_id', models.CharField(max_length=14)),
                ('dest_store_nbr', models.CharField(max_length=3)),
                ('dc_sel_section_id', models.CharField(max_length=6, null=True)),
                ('label_create_ts', models.DateTimeField()),
                ('shipping_tag_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('rcv_unit_tag_id', models.CharField(max_length=21)),
                ('item_nbr', models.CharField(max_length=6)),
                ('item1_desc', models.CharField(max_length=20)),
                ('dpto_name', models.CharField(max_length=30)),
                ('ship_unit_qty', models.IntegerField()),
                ('ship_unit_stat_cd', models.IntegerField()),
                ('shipunit_stat_desc', models.CharField(max_length=30)),
                ('cur_loc_slot_id', models.CharField(max_length=11)),
                ('last_change_userid', models.CharField(max_length=15)),
                ('last_change_ts', models.DateTimeField(auto_now=True)),
                ('create_ts', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'auditoria diaria',
                'verbose_name_plural': 'auditorias diarias',
                'db_table': 'auditorias_diarias',
                'ordering': ['-create_ts'],
            },
        ),
    ]
