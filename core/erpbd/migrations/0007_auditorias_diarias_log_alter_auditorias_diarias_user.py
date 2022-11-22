# Generated by Django 4.1 on 2022-11-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erpbd', '0006_alter_auditorias_diarias_user_and_more'),
    ]

    operations = [
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
        migrations.AlterField(
            model_name='auditorias_diarias',
            name='user',
            field=models.CharField(choices=[('j0c0af6', 'j0c0af6'), ('v0j0af6', 'v0j0af6'), ('C0j0a56', 'C0j0a56'), ('Z0j0a30', 'Z0j0a30')], default='No Asign', max_length=8, verbose_name='Auditor'),
        ),
    ]
