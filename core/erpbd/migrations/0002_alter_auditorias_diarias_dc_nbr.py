# Generated by Django 4.1 on 2022-09-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpbd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorias_diarias',
            name='dc_nbr',
            field=models.CharField(max_length=5),
        ),
    ]
