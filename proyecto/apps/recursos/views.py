from django.shortcuts import render

# Create your views here.
def Listar_recursos(request):
  return render(request, 'recursos/listar_recursos.html')