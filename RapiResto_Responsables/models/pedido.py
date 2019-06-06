from django.db import models
from datetime import datetime
from .mesa import Mesa

class Pedido(models.Model):

    id          = models.AutoField(primary_key=True)
    mesa        = models.ForeignKey(Mesa, on_delete=models.CASCADE, null=False)
    fecha       = models.DateTimeField(default = datetime.now)
    total       = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['mesa', 'fecha']

    def __str__(self):
        return str(str(self.id) + ' ' + str(self.mesa) + ' ' + str(self.fecha))
