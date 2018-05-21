from django.db import models
from proyecto.Apps.Administracion.models import Trabajador

# Create your models here.

class VentaFactura (models.Model):
    Producto = models.CharField(max_length=35)
    Precio = models.PositiveSmallIntegerField()
    Vendedor = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    FechaVenta = models.DateField()

    def VentaFactura(self):
        cadena = "{0}, {1}: S/.{2}"
        return cadena.format(self.Vendedor.Nombre, self.Producto, self.Precio)

    def __str__(self):
        return self.VentaFactura()

