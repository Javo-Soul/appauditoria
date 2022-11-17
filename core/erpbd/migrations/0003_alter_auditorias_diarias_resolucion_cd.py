# Generated by Django 4.1 on 2022-11-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpbd', '0002_auditorias_diarias_resolucion_cd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorias_diarias',
            name='resolucion_cd',
            field=models.CharField(choices=[('1', 'Pendiente'), ('2', 'En Progreso'), ('3', 'Terminado'), ('4', 'Cancelado')], default='Pendiente', max_length=13),
        ),
    ]