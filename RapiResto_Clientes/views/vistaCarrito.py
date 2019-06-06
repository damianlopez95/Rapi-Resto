from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from RapiResto_Clientes.forms import AlimentoIDForm
from RapiResto_Responsables.models import Alimento, AlimentoPedido, Pedido, Mesa

class VistaCarrito(View):

    def getCarrito(request):

        form = AlimentoIDForm()
        alimentos = request.session['alimentos']
        lista = {}
        total = 0
        for alimentoID, cantidad in alimentos.items():
            alimento = Alimento.objects.get(id = int(alimentoID))
            subtotal = getattr(alimento, 'precio')*cantidad
            lista[alimento] = [cantidad, subtotal]
            total += subtotal

        return render(request, "carrito.html", {
            'form'  : form,
            'lista' : lista,
            'total' : total
        })

    def delete(request):

        if request.method == 'POST':
            form = AlimentoIDForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data['alimento']
                request.session['alimentos'].pop(str(id),None)
                request.session.modified = True 
                return HttpResponseRedirect('/carrito')

    def confPedido(request):

        if request.method == 'POST':
            if request.session['alimentos'] != {}:
                alimentos = request.session['alimentos']
                mesaID = request.session['mesa']
                mesa = Mesa.objects.get(id=mesaID)
                pedido = Pedido.objects.create(mesa=mesa)
                total = 0
                for alimentoID, cantidad in alimentos.items():
                    alimento = Alimento.objects.get(id = int(alimentoID))
                    subtotal = getattr(alimento, 'precio')*cantidad
                    total += subtotal
                    alimentopedido = AlimentoPedido.objects.create(alimento=alimento, cantidad=cantidad, pedido=pedido, subtotal=subtotal)
                pedido = Pedido.objects.update(total=total)
                request.session.flush()
                #Actualizar stock de alimentos
                # messages.info(request, 'Gracias por su compra. En minutos llegará su pedido..')
                #Se notifica al encargado del pedido
            return HttpResponseRedirect('/sucursales')

