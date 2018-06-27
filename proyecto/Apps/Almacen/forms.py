from django import forms
from proyecto.Apps.Almacen.models import Ingreso

class IngresoForm(forms.ModelForm):
    class Meta:
        model = Ingreso

        fields = [
            'Proveedor',
            'Producto',
            'PrecioCompra',
            'FechaIngreso',
        ]
        labels = {
            'Proveedor': 'Proveedor',
            'Producto': 'Producto',
            'PrecioCompra': 'Precio Compra',
            'FechaIngreso': 'FechaIngreso',
        }
        widgets = {
            'Proveedor': forms.Select(attrs={'class':'form-control'}),
            'Producto': forms.Select(attrs={'class':'form-control'}),
            'PrecioCompra': forms.TextInput(attrs={'class':'form-control'}),
            'FechaIngreso': forms.DateInput(attrs={'class':'form-control'}),
        }