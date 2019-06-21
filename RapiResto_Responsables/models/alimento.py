import os
from django.db import models
from .categoria import Categoria
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

class Alimento(models.Model):

    nombre          = models.CharField(max_length=80, unique=True, blank=False)
    descripcion     = models.TextField(blank=True)
    precio          = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    categoria       = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=False)
    recomendaciones = models.ManyToManyField('self', blank=True)
    imagen          = models.ImageField(blank=True, null=True, upload_to='optimized_images/')

    class Meta:
        ordering = ['categoria', 'nombre']

    def __str__(self):
        return str(self.nombre)

    def save(self, *args, **kwargs):

        if self.imagen:
            try:
                this = Alimento.objects.get(id=self.id)
                if this.imagen != self.imagen:
                    if 'optimized_images' not in self.imagen.path:
                        print(self.imagen.path)
                        imagen = Image.open(self.imagen)
                        resize = imagen.resize((1280, 720), Image.ANTIALIAS)
                        new_image = BytesIO()
                        resize.save(new_image, format=imagen.format, quality=75)
                        temp_name = self.imagen.name
                        self.imagen.save(temp_name, content=ContentFile(new_image.getvalue()), save=False)
            except:
                if 'optimized_images' not in self.imagen.path:
                    imagen = Image.open(self.imagen)
                    resize = imagen.resize((1280, 720), Image.ANTIALIAS)
                    new_image = BytesIO()
                    resize.save(new_image, format=imagen.format, quality=75)
                    temp_name = self.imagen.name
                    self.imagen.save(temp_name, content=ContentFile(new_image.getvalue()), save=False)
        super(Alimento, self).save(*args, **kwargs)

