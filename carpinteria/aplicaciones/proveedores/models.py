from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    pais = models.CharField(max_length=100, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)