from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView
from .models import *


class trabajadordefecto(TemplateView):
    template_name = 'trabajadordefecto.html'

class creartrabajadores(CreateView):
    template_name = 'crear_trabajadores.html'
    model = Trabajador
    fields = '__all__'
    success_url = '/trabajadores/listar_trabajadores/'
