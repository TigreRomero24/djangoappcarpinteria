from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *


class creartrabajadores(CreateView):
    template_name = 'crear_trabajadores.html'
    model = Trabajador
    fields = '__all__'
    success_url = '/trabajadores'

class listartrabajadores(ListView):
    template_name = 'listar_trabajadores.html'
    model = Trabajador
    context_object_name = 'trabajadores'

class actualizar_trabajador(UpdateView):
    template_name = 'actualizar_trabajador.html'
    model = Trabajador
    fields = '__all__'
    success_url = '/trabajadores'

class eliminar_trabajador(DeleteView):
    template_name = 'eliminar_trabajador.html'
    model = Trabajador
    success_url = '/trabajadores'
    context_object_name = 'trabajador'
