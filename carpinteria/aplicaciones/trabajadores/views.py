from django.shortcuts import render
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView
from .models import *


class creartrabajadores(CreateView):
    template_name = 'crear_trabajadores.html'
    model = Trabajador
    fields = '__all__'
    success_url = '/ver_trabajador'

    def form_valid(self, form):
        return render(self.request, 'crear_trabajadores.html', {'form': form})

class listartrabajadores(ListView):
    template_name = 'listar_trabajadores.html'
    model = Trabajador
    context_object_name = 'trabajadores'

    