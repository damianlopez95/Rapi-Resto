from django.db import models
from .categoria import Categoria

class Alimento(models.Model):

    nombre          = models.CharField(max_length=80, unique=True, blank=False)
    descripcion     = models.TextField(blank=True)
    precio          = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    categoria       = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    recomendaciones = models.ManyToManyField('self', blank=True)
    imagen          = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return str(self.nombre)
