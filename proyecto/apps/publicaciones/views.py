from django.shortcuts import render

# Create your views here.
def Listar_publicaciones(request):
  return render(request, 'publicaciones/listar_publicaciones.html')