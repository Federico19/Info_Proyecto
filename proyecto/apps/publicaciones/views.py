from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Publicacion

# Create your views here.

@login_required
def Listar_Publicaciones(request):
    contexto = {}

    n = Publicacion.objects.all() #RETORNA LISTA DE OBJETOS

    contexto['publicaciones'] = n


    #n = Publicacion.objects.all()
    #print(f"TODAS: {n}")

    #x = Publicacion.objects.get(pk = 1)
    #print(f"1 SOLA: {x}")
    

    #f = Publicacion.objects.filter(categoria_noticia = 3)
    #print(f"SOLO DEPORTES: {f}")

    return render(request, 'publicaciones/listar_publicaciones.html', contexto)

@login_required
def Detalle_Publicaciones(request, pk):
    contexto = {}

    n = Publicacion.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto['publicacion'] = n

    return render(request, 'publicaciones/detalle.html', contexto)