from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Trabajador(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False)
    cedula = models.CharField(max_length=10,validators=[RegexValidator(r'^\d{10}$')] , unique=True, blank=False, null=False)
    codigo_empleado = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')], unique=True, blank=False, null=False)
    imagen = models.ImageField(upload_to='imgtrabajadores')

