from django.shortcuts import render
import json as simplejson
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from RapiResto_Clientes.forms import MesaForm
from RapiResto_Responsables.models import Sucursal, Pedido, Mesa

class VistaSucursales(View):

    def obtenerSucursales(request):
    
        form = MesaForm()
        if request.method == 'POST':
            form = MesaForm(request.POST)
            if form.is_valid():
                request.session.flush()
                mesa = Mesa.objects.get(numero=form.cleaned_data['mesa'], sucursal=form.cleaned_data['sucursal'])
                request.session['mesa'] = mesa.id
                request.session['sucursal'] = mesa.sucursal.numero
                request.session['alimentos'] = {}
                request.session['items'] = 0
                return HttpResponseRedirect(str(mesa.sucursal.numero) + '/cartas')

        sucursales = Sucursal.objects.all()
        coordenadas = serializers.serialize('json', list(sucursales), fields=('direccion','latitud','longitud'))
        return render(request, 'sucursales.html', {
            "sucursales":sucursales,
            "coordenadas":coordenadas,
            "form":form
        })

    def obtenerMesas(request):

        dato_sucursal = request.GET['suc']
        respuesta = int(dato_sucursal.split()[0])
        sucursal = Sucursal.objects.get(numero=respuesta)
        mesas = serializers.serialize('json', list(sucursal.mesas.all()))
        return HttpResponse(mesas, content_type='application/json')
