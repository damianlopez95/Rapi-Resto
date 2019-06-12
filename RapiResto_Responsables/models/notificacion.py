from django.db import models
from .usuario import Usuario
from .pedido import Pedido

class Notificacion(models.Model):

    pedido      = models.ForeignKey(Pedido, on_delete=models.CASCADE, default=None)
    usuario     = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=False)
    leido       = models.BooleanField(default=False)

