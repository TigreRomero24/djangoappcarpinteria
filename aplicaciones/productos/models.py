from django.db import models

class Producto(models.Model):
    IVA_CHOICES = [
        (0, '0%'),
        (15, '15%'),
    ]
    nombre = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.CharField(max_length=200, blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    iva = models.IntegerField(choices=IVA_CHOICES, default=15)
    imagen = models.ImageField(upload_to='imgproducts')

    def __str__(self):
        return self.nombre 