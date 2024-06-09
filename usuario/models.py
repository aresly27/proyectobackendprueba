from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    def create_user(self, correo, nombre, contrasena=None):
        if not correo:
            raise ValueError('El usuario debe tener un correo electrónico')

        usuario = self.model(
            correo=self.normalize_email(correo),
            nombre=nombre,
        )
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario


class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length=120, verbose_name="Nombre")
    correo = models.EmailField(verbose_name="Correo Electronico", unique=True)
    fecha_nac = models.DateField(verbose_name="Fecha de Nacimiento")
    usuario = models.CharField(max_length=120, verbose_name="Usuario")
    imagen = models.CharField(max_length=120, verbose_name="Imagen")
    created_date = models.DateField(auto_now_add=True, verbose_name="Fecha de creación")
    status = models.BooleanField(default=True, verbose_name="Estatus")
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'correo'
    REQUIRED_FIELDS = ['nombre']
    
    def __str__(self):
        return self.correo
    
    
    class Meta:
        db_table = 'usuario'