# Generated by Django 5.0.6 on 2024-06-09 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_alter_usuario_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='status',
            field=models.BooleanField(default=True, verbose_name='Estatus'),
        ),
    ]
