# Generated by Django 5.0.6 on 2024-06-28 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario', '0003_alter_usuario_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(verbose_name='Titulo')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('area', models.CharField(verbose_name='Area')),
                ('descripcion', models.CharField(verbose_name='Descripcion')),
                ('imagen', models.CharField(max_length=120, verbose_name='Imagen')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario.usuario', verbose_name='user_id')),
            ],
            options={
                'db_table': 'logro',
            },
        ),
    ]
