from django import forms

from RapiResto_Responsables.models import Alimento, Mesa, Sucursal

class AlimentoForm(forms.ModelForm):
    
    class Meta:
        model = Alimento
        fields = ("nombre","descripcion","precio","categoria","recomendaciones", "imagen")

class MesaForm(forms.Form):

    mesa = forms.IntegerField()
    sucursal = forms.IntegerField()

class PedidoAlimentoForm(forms.Form):

    alimento = forms.CharField()
    cantidad = forms.IntegerField()

class AlimentoIDForm(forms.Form):

    alimento = forms.IntegerField()
