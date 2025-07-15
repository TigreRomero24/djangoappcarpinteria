from django import forms
from .models import Empresa

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'yearfunda': forms.DateInput(attrs={'type': 'date'}),
        }