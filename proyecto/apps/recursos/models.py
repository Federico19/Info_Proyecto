from django.db import models

class Recurso(models.Model):
  nombre = models.CharField(max_length=150)
  archivo = models.FileField(blank=True, null=True)
  fecha = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nombre