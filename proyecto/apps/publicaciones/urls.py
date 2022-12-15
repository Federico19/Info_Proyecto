from django.urls import path

from . import views

app_name = 'publicaciones'
urlpatterns = [
   path('', views.Listar_Publicaciones, name = 'listar_publicaciones'),

   path('Detalle/<int:pk>/', views.Detalle_Publicaciones, name = 'detalle'),
   path('Detalle/<int:pk>/AgregarComentario/', views.Agregar_Comentario, name = 'agregar_comentario'),

]