from django.db import models
from .alimento import Alimento
from .carta import Carta

class AlimentoCarta(models.Model):

    alimento    = models.ForeignKey(Alimento, on_delete=models.CASCADE, null=False)
    stock       = models.PositiveIntegerField(default=0, blank=False)
    carta       = models.ForeignKey(Carta, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return ('Carta ' + str(self.carta) + ' | Alimento ' + str(self.alimento))
