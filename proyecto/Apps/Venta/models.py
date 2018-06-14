from django.db import models
from proyecto.Apps.Administracion.models import Trabajador
from proyecto.Apps.Almacen.models import Salida

# Create your models here.
class Cliente (models.Model):
    Nombre = models.CharField(max_length=25)
    Apellidos = models.CharField(max_length=25)
    DNI = models.CharField(max_length=8)
    SEXO = (('M', 'masculino'), ('F', 'femenino'))
    Sexo = models.CharField(max_length=10, choices=SEXO, default='masculino')

    def Cliente(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Nombre, self.DNI)

    def __str__(self):
        return self.Cliente()


class VentaFactura (models.Model):
    Producto = models.ManyToManyField(Salida, blank=True)
    Precio = models.PositiveSmallIntegerField()
    Igv = models.PositiveSmallIntegerField()
    Vendedor = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, null=False, blank=False, on_delete=models.CASCADE)
    FechaVenta = models.DateField()

    def VentaFactura(self):
        cadena = "{0}, {1}: S/.{2}"
        return cadena.format(self.Vendedor.Nombre, self.Producto, self.Precio)

    def __str__(self):
        return self.VentaFactura()


