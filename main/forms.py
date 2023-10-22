from django import forms
from .models import *

class FrmCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["dni", "nombre", "apellido"]
