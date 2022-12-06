from django.db import models

class Categoria(models.Model):
  nombre = models.CharField(max_Length = 60)

class Noticia(models.Model):
  titulo = models.CharField(max_lenght = 150, null = False)
  cuerpo = models.TextField()
  imagen = models.ImageField(upload_to='noticias') #ya sabe que en media tiene que ubicarse
  categortia_noticia = models.ForeignKey(Categoria, on_delete = models.CASCADE)
  fecha = models.DateTimeField(auto_now_add = True)

  def __str__(self):
    return self.titulo