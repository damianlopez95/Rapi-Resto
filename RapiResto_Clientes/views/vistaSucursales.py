from django.shortcuts import render
import json as simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from RapiResto_Clientes.forms import MesaForm
from RapiResto_Responsables.models import Sucursal, Pedido, Mesa

class VistaSucursales(View):

    def getSucursales(request):
    
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
                return HttpResponseRedirect('/cartas/' + str(mesa.sucursal.numero))

        sucursales = Sucursal.objects.all()
        return render(request, 'sucursales.html', {
            "sucursales":sucursales,
            "form":form
        })


    def getMesas(request):

        dato_sucursal = request.GET['suc']
        mesas = []
        resultado = []
        respuesta = int(dato_sucursal.split()[0])
        sucursal = Sucursal.objects.get(numero=respuesta)
        mesas = sucursal.mesas.all()
        for mesa in mesas:
            resultado.append({'mesa':mesa.numero})
        return HttpResponse(simplejson.dumps(resultado), content_type='application/json')
