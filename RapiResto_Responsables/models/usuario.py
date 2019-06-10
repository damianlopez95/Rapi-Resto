from django.db import models
from django.contrib.auth.models import User

from RapiResto_Responsables.models import Sucursal

class Usuario(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, blank=True, null=True)

