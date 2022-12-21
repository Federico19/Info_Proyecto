from django.shortcuts import render
from .models import Recurso 
from django.http import HttpResponse

# Esta vista permite listar los recursos que estan en la BD, y tambien permite el poder descargarlos.
def Listar_recursos(request):
  recursos = Recurso.objects.all().order_by('fecha')

  contexto = {
    'recursos' : recursos,
  }

  id_recurso = request.POST.get('id_recurso', None)

  if id_recurso:
    recurso = Recurso.objects.get(pk = id_recurso)
    response = HttpResponse(recurso.archivo, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="%s"' % recurso.archivo
    return response

  return render(request, 'recursos/listar_recursos.html', contexto)


'''
def Descargar_Recurso(request):
  id_recurso = request.POST.get('id_recurso')
  recurso = Recurso.objects.get(pk = id_recurso)

  response = HttpResponse(recurso.archivo, content_type='text/plain')
  response['Content-Disposition'] = 'attachment; filename="%s"' % recurso.archivo
  return response
  '''
