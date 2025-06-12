from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import *


class productos_defecto(TemplateView):
    template_name = 'productos_defecto.html'

class producto_nuevo(CreateView):
    template_name = 'producto_nuevo.html'
    model = Producto
    fields = '__all__'
    success_url = '/productos/'