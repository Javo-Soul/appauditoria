# Generated by Django 4.1 on 2022-11-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpbd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditorias_diarias',
            name='resolucion_cd',
            field=models.CharField(choices=[('1', '1.1'), ('2', '2.1'), ('3', '3.1')], default='1.1', max_length=3),
        ),
    ]