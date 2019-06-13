from django.shortcuts import render
from django.views.generic import View

from RapiResto_Clientes.forms import PedidoAlimentoForm
from RapiResto_Responsables.models import Carta, Sucursal, AlimentoCarta, Alimento, AlimentoPedido

class VistaCarta(View) :

    def obtenerAlimentos(request, pkcarta):

        form = PedidoAlimentoForm()
        sucursal = request.session['sucursal']
        alimentosCarta = AlimentoCarta.objects.filter(carta = pkcarta)
        return render(request, "carta.html", {
            "alimentosCarta" : alimentosCarta,
            "sucursal": sucursal,
            "form" : form
        })

class VistaCartas(View) :

    def get(self, request, pksucursal):
        sucursalAux = Sucursal.objects.get(pk = pksucursal)
        cartas = Carta.objects.filter(sucursal = sucursalAux)
        return render(request, "cartas.html", {
            "cartas" : cartas
        })
