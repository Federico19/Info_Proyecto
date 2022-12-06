from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import RegistroForm

class Registro(CreateView):
  #Formulario Django
  form_class = RegistroForm
  success_url = reverse_lazy('login')
  tempalte_name = 'usuarios/registro.html'
