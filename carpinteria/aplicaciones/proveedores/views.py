from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import *


class proveedor_nuevo(CreateView):
    template_name = 'proveedor_nuevo.html'
    model = Proveedor
    fields = '__all__'
    success_url = '/productos/'

class listar_proveedores(ListView):
    template_name = 'listar_proveedores.html'
    model = Proveedor
    context_object_name = 'proveedores'