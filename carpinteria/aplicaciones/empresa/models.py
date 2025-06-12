from django.db import models

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=200, blank=True, null=True)
    direccion = models.TextField(blank=True, null=True)
    mision = models.TextField(blank=True, null=True)
    vision = models.TextField(blank=True, null=True)
    yearfunda = models.IntegerField(blank=True, null=True)
    ruc = models.CharField(max_length=13, unique=True, blank=True, null=True)
    imagen = models.ImageField(upload_to='imgempresa', blank=True, null=True)