from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView
from .models import *

def inicio(request):
    return render(request, 'inicio.html')

class empresadefecto(TemplateView):
    template_name = 'empresadefecto.html'

class empresanueva(CreateView):
    template_name = 'empresanueva.html'
    model = Empresa
    fields = '__all__'
    success_url = '/empresa/listaempresas/'