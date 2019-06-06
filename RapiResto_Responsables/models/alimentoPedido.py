from django.db import models
from .alimento import Alimento
from .pedido import Pedido

class AlimentoPedido(models.Model):

    alimento    = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=False, blank=False)
    cantidad    = models.PositiveIntegerField(blank=False)
    subtotal    = models.DecimalField(max_digits=7, decimal_places=2, default = 0, null=False, blank=False)
    pedido      = models.ForeignKey(Pedido, related_name="alimentos", on_delete=models.CASCADE, blank=False)

