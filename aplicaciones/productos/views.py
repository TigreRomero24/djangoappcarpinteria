from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import *


class producto_nuevo(CreateView):
    template_name = 'producto_nuevo.html'
    model = Producto
    fields = '__all__'
    success_url = '/productos'

class listar_productos(ListView):
    template_name = 'listar_productos.html'
    model = Producto
    context_object_name = 'productos'

class actualizar_producto(UpdateView):
    template_name = 'actualizar_producto.html'
    model = Producto
    fields = '__all__'
    success_url = '/productos'

class eliminar_producto(DeleteView):
    template_name = 'eliminar_producto.html'
    model = Producto
    success_url = '/productos'
    context_object_name = 'producto'