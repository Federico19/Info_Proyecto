from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Publicacion, Comentario, Categoria
from django.core.paginator import Paginator
from django.urls import reverse_lazy
import datetime

# Create your views here.


def Listar_Publicaciones(request):
    contexto = {}
    cat = Categoria.objects.all().order_by('nombre')

    #Filtro por categoria
    id_categoria = request.GET.get('id', None)

    if id_categoria:
      publicaciones = Publicacion.objects.filter (categoria_publicacion = id_categoria) #Filtra
    else:
      publicaciones = Publicacion.objects.all() #RETORNA LISTA DE OBJETOS


    #Filtro por fecha de publicacion
    fecha_publicacion = request.GET.get('fecha', None)
        
    publi_fecha = []
    if fecha_publicacion:
      publicaciones = Publicacion.objects.all()
      print(type(publicaciones))
      for publi in publicaciones:
        if str(publi.fecha.date()) == fecha_publicacion:
          print('Funka pa')
          publi_fecha.append(publi)
     
      publicaciones = publi_fecha


    #Define los elementos para la paginacion
    paginator = Paginator(publicaciones, 2)
    pagina = request.GET.get('page')
    publicaciones = paginator.get_page(pagina)


    contexto={
      'publicaciones': publicaciones,
      'categoria' : cat
    }


    #n = Publicacion.objects.all()
    #print(f"TODAS: {n}")

    #x = Publicacion.objects.get(pk = 1)
    #print(f"1 SOLA: {x}")
    

    #f = Publicacion.objects.filter(categoria_noticia = 3)
    #print(f"SOLO DEPORTES: {f}")

    return render(request, 'publicaciones/listar_publicaciones.html', contexto)


def Detalle_Publicaciones(request, pk):
    contexto = {}

    publicacion = Publicacion.objects.get(pk = pk) #RETORNA SOLO UN OBJETO
    contexto={
      'publicacion': publicacion
    }

    return render(request, 'publicaciones/detalle.html', contexto)

@login_required
def Comentar(request):
  id_publicacion = request.POST.get('id_publicacion', None)
  publi = Publicacion.objects.get(pk = id_publicacion)
  cuerpo_comentario = request.POST.get('comentario', None)
  nombre_usuario = request.user.username
  comentario = Comentario.objects.create(publicacion = publi, nombre = nombre_usuario, cuerpo = cuerpo_comentario)

  return redirect(reverse_lazy('publicaciones:detalle', kwargs={'pk': id_publicacion}))
