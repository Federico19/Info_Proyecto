from django.urls import path

from . import views

app_name = 'publicaciones'
urlpatterns = [
   path('', views.Listar_Publicaciones, name = 'listar_publicaciones'),

   path('Detalle/<int:pk>', views.Detalle_Publicaciones, name = 'detalle'),
   path('Comentar/', views.Comentar, name = 'comentar'),
]