from django.db import models
from .sucursal import Sucursal
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

class Carta(models.Model):

    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=75, blank=False, default=None)
    sucursal    = models.ForeignKey(Sucursal, on_delete=models.CASCADE, null=False)
    imagen      = models.ImageField(blank=True, null=True, upload_to='optimized_images/')

    class Meta:
        unique_together = (('nombre','sucursal'))
        ordering = ['sucursal', 'nombre']

    def __str__(self):
        return str((self.nombre) + ' Suc: ' + str(self.sucursal.numero))

    def save(self, *args, **kwargs):
        if self.imagen:
            try:
                this = Carta.objects.get(id=self.id)
                if this.imagen != self.imagen:
                    if 'optimized_images' not in self.imagen.path:
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
        super(Carta, self).save(*args, **kwargs)

