from django.db import models
from usuario.models import Usuario

# Create your models here.
class Login(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
