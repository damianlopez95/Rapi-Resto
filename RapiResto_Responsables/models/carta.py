from django.db import models
from .sucursal import Sucursal

class Carta(models.Model):

    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=75, blank=False, default=None)
    sucursal    = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=False)
    imagen      = models.ImageField(blank=True, null=True)

    class Meta:
        unique_together = (('nombre','sucursal'))
        ordering = ['sucursal', 'nombre']

    def __str__(self):
        return str((self.nombre) + ' Suc: ' + str(self.sucursal.numero))

 