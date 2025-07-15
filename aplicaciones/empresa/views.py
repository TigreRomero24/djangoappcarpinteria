from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import EmpresaForm

def inicio(request):
    return render(request, 'inicio.html')

class empresanueva(CreateView):
    template_name = 'empresanueva.html'
    model = Empresa
    form_class = EmpresaForm
    success_url = '/empresa'

class listar_empresa(ListView):
    template_name = 'listar_empresa.html'
    model = Empresa
    context_object_name = 'empresa'

class actualizar_empresa(UpdateView):
    template_name = 'actualizar_empresa.html'
    model = Empresa
    fields = '__all__'
    success_url = '/empresa'

class eliminar_empresa(DeleteView):
    template_name = 'eliminar_empresa.html'
    model = Empresa
    success_url = '/empresa'
    context_object_name = 'empresa'