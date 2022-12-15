from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Publicacion
from django.core.paginator import Paginator

# Create your views here.

@login_required
def Listar_Publicaciones(request):
    contexto = {}

    publicaciones = Publicacion.objects.all() #RETORNA LISTA DE OBJETOS

    paginator = Paginator(publicaciones, 1)
    pagina = request.GET.get('page')
    publicaciones = paginator.get_page(pagina)

    contexto={
      'publicaciones': publicaciones
    }


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

    publicacion = Publicacion.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto={
      'publicacion': publicacion
    }

    return render(request, 'publicaciones/detalle.html', contexto)