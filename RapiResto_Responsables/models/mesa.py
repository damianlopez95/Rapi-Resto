from django.db import models
from django.core.validators import MinValueValidator
from .sucursal import Sucursal

class Mesa(models.Model):

    numero      = models.PositiveIntegerField(validators = [MinValueValidator(1)])
    sucursal    = models.ForeignKey(Sucursal, related_name="mesas", on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = (('numero', 'sucursal'))
        ordering = ['sucursal', 'numero']

    def __str__(self):
        return ('Mesa: ' + str(self.numero) + '  Suc: ' + str(self.sucursal.numero))

