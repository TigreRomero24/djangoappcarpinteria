from django.db import models

# Create your models here.
class Producto(models.Model):
    IVA_CHOICES = [
        (0, '0%'),
        (15, '15%'),
    ]

    nombre = models.CharField(max_length=100, blank=True, null=True)
    descripcion = models.TextField(max_length=500, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    iva = models.IntegerField(choices=IVA_CHOICES, default=15)
    imagen = models.ImageField(upload_to='imgproductos', blank=True, null=True)