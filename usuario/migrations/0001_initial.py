# Generated by Django 5.0.6 on 2024-06-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo Electronico')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('usuario', models.CharField(max_length=120, verbose_name='Usuario')),
                ('password', models.CharField(max_length=120, verbose_name='Contraseña')),
                ('imagen', models.CharField(max_length=120, verbose_name='Imagen')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('status', models.BooleanField(default=True, verbose_name='Estatus')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
