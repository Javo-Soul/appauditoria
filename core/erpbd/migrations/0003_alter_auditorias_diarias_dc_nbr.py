# Generated by Django 4.1 on 2022-09-12 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpbd', '0002_alter_auditorias_diarias_dc_nbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditorias_diarias',
            name='dc_nbr',
            field=models.CharField(max_length=10),
        ),
    ]