from django.contrib import admin
from proyecto.Apps.Almacen.models import *

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Ingreso)
admin.site.register(Salida)