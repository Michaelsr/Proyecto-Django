from django.db import models

# Create your models here.


class Proveedor(models.Model):
    NombreProveedor = models.CharField(max_length=35)
    Ruc = models.CharField(max_length=11)
    Direccion = models.CharField(max_length=35)
    Telefono = models.CharField(max_length=9)
    DatosEncargado = models.CharField(max_length=35)
    TelefonoEncargado = models.CharField(max_length=9)
    FechaRegistro = models.DateField()


    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.NombreProveedor, self.Telefono, self.Direccion)

    def __str__(self):
        return self.NombreCompleto()

class Producto(models.Model):
    NombreProducto = models.CharField(max_length=35)
    Unidad = models.PositiveSmallIntegerField()
    Estado = models.BooleanField(default=True)

    CATEGORIA = (('LACTEOS', 'lagteos'), ('GALLETAS', 'galletas'), ('GOLOSINAS', 'golosinas'), ('CONCERVAS', 'concerva'),('BEBIDAS', 'bebidas'), ('OTROS', 'otros'))
    Categoria = models.CharField(max_length=10, choices=CATEGORIA, default='LASTEOS')

    def __str__(self):

        return "{0} ({1})".format(self.NombreProducto, self.Unidad)

class Ingreso(models.Model):
    Proveedor = models.ForeignKey(Proveedor, null=False, blank=False, on_delete=models.CASCADE)
    Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    FechaIngreso = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        cadena = "Proveedor: {0} >>> Producto: {1} >>> Unidad: ({2}) >>> Fecha {3} "
        return cadena.format(self.Proveedor.NombreProveedor, self.Producto.NombreProducto, self.Producto.Unidad, self.FechaIngreso)


class Salida(models.Model):
    Producto = models.ForeignKey(Producto, null=False, blank=False, on_delete=models.CASCADE)
    FechaSalida = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        cadena = "{0}, {1}"
        return cadena.format(self.Producto.NombreProducto, self.FechaSalida)