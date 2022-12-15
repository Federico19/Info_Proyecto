from django.urls import path
from .views import *


app_name = 'noticias'
urlpatterns = [
    path('', Listar_Noticias, name = 'listar'),
]
