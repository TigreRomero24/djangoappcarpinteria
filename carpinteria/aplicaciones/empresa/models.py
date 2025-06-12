from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.CharField(max_length=300, blank=True, null=True)
    mision = models.CharField(max_length=300, blank=True, null=True)
    vision = models.CharField(max_length=300, blank=True, null=True)
    yearfunda = models.IntegerField(blank=True, null=True, verbose_name="Año de Fundación")
    ruc = models.CharField(max_length=13, unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='imgempresa', blank=True, null=True)