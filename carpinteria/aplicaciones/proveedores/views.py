from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import *


class proveedores_defecto(TemplateView):
    template_name = 'proveedores_defecto.html'

class proveedor_nuevo(CreateView):
    template_name = 'proveedor_nuevo.html'
    model = Proveedor
    fields = '__all__'
    success_url = '/productos/'

