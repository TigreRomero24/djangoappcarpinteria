from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import *


class proveedor_nuevo(CreateView):
    template_name = 'proveedor_nuevo.html'
    model = Proveedor
    fields = '__all__'
    success_url = '/proveedores'

class listar_proveedores(ListView):
    template_name = 'listar_proveedores.html'
    model = Proveedor
    context_object_name = 'proveedores'

class actualizar_proveedor(UpdateView):
    template_name = 'actualizar_proveedor.html'
    model = Proveedor
    fields = '__all__'
    success_url = '/proveedores'

class eliminar_proveedor(DeleteView):
    template_name = 'eliminar_proveedor.html'
    model = Proveedor
    success_url = '/proveedores'
    context_object_name = 'proveedor'
    