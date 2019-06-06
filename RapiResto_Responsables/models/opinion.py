from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .sucursal import Sucursal

class Opinion(models.Model):

    nombre      = models.CharField(max_length=25, default='Anónimo')
    comentario  = models.TextField(blank=True)
    valoracion  = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)], blank=False)
    sucursal    = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=False)

    class Meta:
        ordering = ['valoracion']
