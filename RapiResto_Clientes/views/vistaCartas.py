from django.shortcuts import render
from django.views.generic import View
from django.core import serializers

from RapiResto_Clientes.forms import PedidoAlimentoForm
from RapiResto_Responsables.models import Carta, Sucursal, AlimentoCarta, Alimento, AlimentoPedido

class VistaCarta(View) :

    def getAlimento(request, pkcarta):

        form = PedidoAlimentoForm()
        if request.method == 'POST':
            form = PedidoAlimentoForm(request.POST)
            if form.is_valid():
                contenido = {
                    'alimentoID' : form.cleaned_data['alimento'],
                    'cantidad' : form.cleaned_data['cantidad']
                }
                if  contenido['alimentoID'] in request.session['alimentos']:
                        cant = request.session['alimentos'][contenido['alimentoID']]
                        request.session['alimentos'][contenido['alimentoID']] = contenido['cantidad'] + cant
                else :
                        request.session['alimentos'][contenido['alimentoID']] = contenido['cantidad']
                alimentos = request.session['alimentos']
                request.session.modified = True 

        alimentosCarta = AlimentoCarta.objects.filter(carta = pkcarta)
        return render(request, "carta.html", {
            "alimentosCarta" : alimentosCarta,
            "form" : form
        })

class VistaCartas(View) :

    def get(self, request, pksucursal):
        sucursalAuxiliar = Sucursal.objects.get(pk = pksucursal)
        cartas = Carta.objects.filter(sucursal = sucursalAuxiliar)
        return render(request, "cartas.html", {
            "cartas" : cartas
        })
