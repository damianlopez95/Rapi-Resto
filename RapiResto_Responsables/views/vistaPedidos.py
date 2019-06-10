from django.shortcuts import render
from django.views.generic import View

from RapiResto_Responsables.models import Pedido, AlimentoPedido

class VistaPedido(View) :

    def obtenerPedidos(request):

        pedidos = Pedido.objects.all()
        return render(request,"listaPedidos.html", {
        "pedidos" : pedidos
     })

    def verPedido(request, pkpedido):

        pedido = Pedido.objects.get(pk=pkpedido)
        alimentos = AlimentoPedido.objects.filter(pedido=pedido)
        return render(request,"verPedido.html", {
        "pedido" : pedido,
        "alimentos" : alimentos
     })

