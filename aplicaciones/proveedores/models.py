from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False)
    descripcion = models.CharField(max_length=500, blank=False, null=False)
    telefono = models.CharField(max_length=12,validators=[RegexValidator(regex=r'^\d{12}$')], blank=False, null=False)
    pais = models.CharField(max_length=100, blank=False, null=False)
    correo = models.EmailField(unique=True, blank=False, null=False)
    direccion = models.CharField(max_length=300, blank=False, null=False)