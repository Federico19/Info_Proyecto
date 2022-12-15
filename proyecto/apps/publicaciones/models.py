from django.db import models


class Categoria(models.Model):
  nombre = models.CharField(max_length = 60)

  def __str__(self):
    return self.nombre


class Publicacion(models.Model):

  titulo = models.CharField(max_length = 150)
  cuerpo = models.TextField()
  imagen = models.ImageField(upload_to = 'publicaciones')
  categoria_publicacion = models.ForeignKey(Categoria, on_delete = models.CASCADE)
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo

class Comentario(models.Model):

  publicacion = models.ForeignKey(Publicacion, related_name="comentarios", on_delete = models.CASCADE)
  nombre = models.CharField(max_length=255)
  cuerpo = models.TextField()
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s - %s' % (self.publicacion.titulo, self.nombre)
