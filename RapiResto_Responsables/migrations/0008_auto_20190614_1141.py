# Generated by Django 2.2.2 on 2019-06-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RapiResto_Responsables', '0007_remove_notificacion_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alimento',
            name='recomendaciones',
            field=models.ManyToManyField(blank=True, null=True, related_name='_alimento_recomendaciones_+', to='RapiResto_Responsables.Alimento'),
        ),
    ]
