from django.db import models

# Create your models here.

class ArticuloModelo(models.Model):
    titulo = models.CharField(max_length=100)
    fecha = models.DateField()
    resumen = models.CharField(max_length=500)
    detalle = models.TextField()
    familia = models.CharField(max_length=1)
    
    def __str__(self):
        return self.titulo + " " + str(fecha) + " " + familia
