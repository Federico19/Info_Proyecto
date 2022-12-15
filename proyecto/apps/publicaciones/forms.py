from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comentario

class FormularioComentario(forms.ModelForm):
  class Meta:
    model = Comentario
    fields = ['cuerpo']
    widgets = {
      'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
    }