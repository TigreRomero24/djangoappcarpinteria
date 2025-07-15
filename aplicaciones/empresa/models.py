from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Empresa(models.Model):
    nombre = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre de la Empresa")
    direccion = models.CharField(max_length=300, blank=False, null=False, verbose_name="Dirección")
    mision = models.CharField(max_length=300, blank=False, null=False, verbose_name="Misión")
    vision = models.CharField(max_length=300, blank=False, null=False, verbose_name="Visión")
    yearfunda = models.DateField(verbose_name="Año de Fundación")
    ruc = models.CharField(max_length=13,validators=[RegexValidator(r'^\d{13}$')], unique=True, blank=False, null=False, verbose_name="RUC")
    imagen = models.ImageField(upload_to='imgempresa', verbose_name="Imagen")