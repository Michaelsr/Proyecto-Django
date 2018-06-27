from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from proyecto.Apps.Almacen.forms import IngresoForm
from proyecto.Apps.Almacen.models import Ingreso


# Create your views here.

def index(request):
    return render(request, 'almacen/index.html')

def almacen_view(request):
    if request.method == 'POST':
        form = IngresoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('almacenIndex:index')
    else:
        form = IngresoForm()

    return render(request, 'almacen/almacen_form.html', {'form':form})

def almacen_list(request):
    ingreso = Ingreso.objects.all()
    contexto = {'imgresos':ingreso}
    return render(request, 'almacen/almacen_list.html', contexto)

def almacen_edit(request, id_ingreso):
    ingreso = Ingreso.objects.get(id=id_ingreso)
    if request.method == 'GET':
        form = IngresoForm(instance=ingreso)
    else:
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
        return redirect('almacenIndex:almacen_listar')
    return render(request, 'almacen/almacen_form.html', {'form':form})

def almacen_delete(request, id_ingreso):
    ingreso = Ingreso.objects.get(id=id_ingreso)
    if request.method == 'POST':
        ingreso.delete()
        return redirect('almacenIndex:almacen_listar')
    return render(request, 'almacen/almacen_delete.html', {'ingreso':ingreso})


class AlmacenList(ListView):
    model = Ingreso
    template_name = 'almacen/almacen_list.html'

class AlmacenCreate(CreateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'almacen/almacen_form.html'
    success_url = reverse_lazy('almacenIndex:almacen_listar')

class AlmacenUpdate(UpdateView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'almacen/almacen_form.html'
    success_url = reverse_lazy('almacenIndex:almacen_listar')

class AlmacenDelete(DeleteView):
    model = Ingreso
    form_class = IngresoForm
    template_name = 'almacen/almacen_delete.html'
    success_url = reverse_lazy('almacenIndex:almacen_listar')
