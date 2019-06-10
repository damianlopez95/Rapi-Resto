from django import forms
from django.contrib.auth.forms import AuthenticationForm

from RapiResto_Responsables.models import Alimento, Mesa, Sucursal, Carta

class AlimentoForm(forms.ModelForm):
    
    class Meta:
        model = Alimento
        fields = ("nombre","descripcion","precio","categoria","recomendaciones", "imagen")

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CartaIDForm(forms.Form):

    carta = forms.IntegerField()

class CartaForm(forms.ModelForm):

    class Meta:
        model = Carta
        fields = ("nombre","sucursal","imagen")

