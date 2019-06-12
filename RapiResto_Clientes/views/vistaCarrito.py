from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
import json as simplejson
from notify.signals import notify

from RapiResto_Clientes.forms import AlimentoIDForm, PedidoAlimentoForm
from RapiResto_Responsables.models import Alimento, AlimentoPedido, Pedido, Mesa, Notificacion, Usuario, AlimentoCarta, Carta

class VistaCarrito(View):

    def obtenerCarrito(request):

        form = AlimentoIDForm()
        alimentos = request.session['alimentos']
        sucursal = request.session['sucursal']
        lista = []
        total = 0
        #lista[0] -> id alimentoCarta // lista[1] -> cantidad
        for alimentoID, lista  in alimentos.items():
            alimento = Alimento.objects.get(id = int(alimentoID))
            subtotal = getattr(alimento, 'precio')*lista[1]
            lista.append({alimento: [lista[1], subtotal]})
            total += subtotal

        return render(request, "carrito.html", {
            'form'  : form,
            'lista' : lista,
            'total' : total,
            "sucursal": sucursal
        })

    def agregarItem(request):

        if request.method == 'POST':
            form = PedidoAlimentoForm(request.POST)
            if form.is_valid():
                contenido = {
                    'alimentocartaID' :form.cleaned_data['alimentoCarta'],
                    'alimentoID' : form.cleaned_data['alimento'],
                    'cantidad' : form.cleaned_data['cantidad']
                }
                print(contenido)
                request.session['items'] = request.session['items'] + contenido['cantidad']
                if  contenido['alimentoID'] in request.session['alimentos']:
                        cant = request.session['alimentos'][contenido['alimentoID']][contenido['cantidad']]
                        request.session['alimentos'][contenido['alimentoID']][contenido['cantidad']] = contenido['cantidad'] + cant
                else :
                        request.session['alimentos'][contenido['alimentoID']] = [contenido['alimentocartaID'], contenido['cantidad']]

        print(request.session['alimentos'])
        mesa = Mesa.objects.get(id = request.session['mesa'])
        return HttpResponseRedirect('cartas/' + str(mesa.sucursal.numero))

    def delete(request):

        if request.method == 'POST':
            form = AlimentoIDForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data['alimento']
                request.session['items'] = request.session['items'] - request.session['alimentos'][str(id)]
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
                for alimentoID, alimentocartaID, cantidad,  in alimentos.items():
                    print(alimentoID, ' ', alimentocartaID, ' ', cantidad)
                #     alimento = Alimento.objects.get(id = int(alimentoID))
                #     subtotal = getattr(alimento, 'precio')*cantidad
                #     total += subtotal
                #     alimentoCarta = AlimentoCarta.objects.get()
                #     cantidadActualizada = alimentoCarta.cantidad - cantidad
                #     alimentoCarta = AlimentoCarta.objects.update(cantidad=cantidadActualizada)
                #     alimentopedido = AlimentoPedido.objects.create(alimento=alimento, cantidad=cantidad, pedido=pedido, subtotal=subtotal)
                # pedido = Pedido.objects.update(total=total)
                # cocinero = Usuario.objects.get(groups__name='Cocinero', sucursal=mesa.sucursal)
                # notificacion = Notificacion(pedido=pedido, usuario=cocinero)
                # notificacion.save()
                # notify.send(recipient = cocinero, verb='Nuevo pedido', nf_type='followed_by_one_user')
                # request.session.flush()
                return HttpResponseRedirect('/')
            return HttpResponseRedirect('carrito')

    def getItems(request):

        resultado = ({'items':request.session['items']})
        return HttpResponse(simplejson.dumps(resultado), content_type='application/json')

