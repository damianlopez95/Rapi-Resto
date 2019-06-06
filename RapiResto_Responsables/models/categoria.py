from django.db import models
from .tipo import Tipo

class Categoria(models.Model):

    nombre  = models.CharField(max_length=50, unique=True)
    tipo    = models.ForeignKey(Tipo, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.nombre)
