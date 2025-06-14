from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView
from .models import *

def inicio(request):
    return render(request, 'inicio.html')


class empresanueva(CreateView):
    template_name = 'empresanueva.html'
    model = Empresa
    fields = '__all__'
    success_url = '/empresa/listaempresas/'

class listar_empresa(ListView):
    template_name = 'listar_empresa.html'
    model = Empresa
    context_object_name = 'empresa'