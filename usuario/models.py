from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo Electronico")
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    usuario = models.CharField(max_length=120, verbose_name="Usuario")
    password = models.CharField(max_length=120, verbose_name="Contraseña")
    imagen = models.CharField(max_length=120, verbose_name="Imagen")
    
    class Meta:
        db_table = 'usuario'