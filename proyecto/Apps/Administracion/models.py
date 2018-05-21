from django.db import models

# Create your models here.

class Trabajador (models.Model):

    Nombre = models.CharField(max_length=25)
    ApellidoPaterno = models.CharField(max_length=25)
    ApellidoMaterno = models.CharField(max_length=25)
    Correo = models.CharField(max_length=40)
    DNI = models.CharField(max_length=8)
    Telefono = models.CharField(max_length=9)
    Cargo = models.CharField(max_length=25)
    FechaIngreso = models.DateField()
    Estado = models.BooleanField(default=True)

    def NombreTrabajador(self):
        cadena = "{0}, {1}, {2}, ({3}),  {4}"
        return  cadena.format(self.Nombre, self.ApellidoPaterno, self.Telefono, self.Cargo, self.Estado)

    def __str__(self):
        return self.NombreTrabajador()


class Usuario(models.Model):
    Correo = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    Password = models.CharField(max_length=25)
    FechaRegistro = models.DateField()


    def NombreUsuario(self):
        cadena = "{0} {1}"
        return cadena.format(self.Correo.Correo, self.FechaRegistro)

    def __str__(self):
        return self.NombreUsuario()