from django.db import models

class Sucursal(models.Model):

    numero      = models.AutoField(primary_key=True)
    direccion   = models.CharField(max_length=75, blank=False, default=None)
    localidad   = models.CharField(max_length=50, blank=False, default=None)
    contacto    = models.CharField(max_length=50, blank=False, default=None)

    def __str__(self):
        return str(str(self.numero) + ' : ' + self.localidad + ' | ' + self.direccion)
