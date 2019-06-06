from django.db import models

class Tipo(models.Model):
    
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.nombre)
