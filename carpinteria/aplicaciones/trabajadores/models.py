from django.db import models

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    apellido = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(unique=True, blank=True, null=True)
    cedula = models.CharField(max_length=10, unique=True, blank=True, null=True)
    codigo_empleado = models.CharField(max_length=20, unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='imgtrabajadores')


# facultad = models.ForeignKey(facultad, on_delete=models.CASCADE)