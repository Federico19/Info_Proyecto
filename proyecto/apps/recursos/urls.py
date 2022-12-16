from django.urls import path

from . import views

app_name = 'recursos'
urlpatterns = [
  path('', views.Listar_recursos ,name='listar'),
  #path('Descargar_Recurso', views.Descargar_Recurso, name = 'descargar'),
]