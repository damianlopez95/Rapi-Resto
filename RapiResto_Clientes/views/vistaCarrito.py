from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
import json as simplejson

from RapiResto_Clientes.forms import AlimentoIDForm, PedidoAlimentoForm
from RapiResto_Responsables.models import Alimento, AlimentoPedido, Pedido, Mesa, Usuario, AlimentoCarta, Carta

class VistaCarrito(View):

    def obtenerCarrito(request):

        form = AlimentoIDForm()
        alimentos = request.session['alimentos']
        sucursal = request.session['sucursal']
        lista = []
        total = 0
        #datos[0] -> id alimentoCarta // datos[1] -> cantidad
        for alimentoID, datos  in alimentos.items():
            alimento = Alimento.objects.get(id = int(alimentoID))
            subtotal = getattr(alimento, 'precio')*datos[1]
            lista.append({'alimentoID': alimento.id,
                          'alimentoNombre': alimento.nombre,
                          'precio': alimento.precio,
                          'cantidad': datos[1],
                          'subtotal': subtotal})
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
                request.session['items'] = request.session['items'] + contenido['cantidad']
                if  contenido['alimentoID'] in request.session['alimentos']:
                        cant = request.session['alimentos'][contenido['alimentoID']][1]
                        request.session['alimentos'][contenido['alimentoID']][1] = contenido['cantidad'] + cant
                else :
                        request.session['alimentos'][contenido['alimentoID']] = [contenido['alimentocartaID'], contenido['cantidad']]

        return HttpResponseRedirect(str(request.session['sucursal']) + '/cartas')

    def eliminarItem(request):

        if request.method == 'POST':
            form = AlimentoIDForm(request.POST)
            if form.is_valid():
                id = form.cleaned_data['alimento']
                request.session['items'] = request.session['items'] - request.session['alimentos'][str(id)][1]
                request.session['alimentos'].pop(str(id),None)
                return HttpResponseRedirect('/carrito')

    def confirmarPedido(request):

        if request.method == 'POST':
            alimentos = request.session['alimentos']
            mesaID = request.session['mesa']
            mesa = Mesa.objects.get(id=mesaID)
            pedido = Pedido.objects.create(mesa=mesa)
            total = 0
            #datos[0] -> id alimentoCarta // datos[1] -> cantidad
            for alimentoID, datos  in alimentos.items():
                alimento = Alimento.objects.get(id = int(alimentoID))
                subtotal = getattr(alimento, 'precio')*datos[1]
                total += subtotal
                alimentoCarta = AlimentoCarta.objects.get(id = datos[0])
                cantidadActualizada = alimentoCarta.stock - datos[1]
                alimentoCarta.stock = cantidadActualizada
                alimentoCarta.save()
                alimentoPedido = AlimentoPedido.objects.create(alimento=alimento, cantidad=datos[1], pedido=pedido, subtotal=subtotal)
            pedido.total = total
            pedido.save()
            return HttpResponseRedirect('/')

    def obtenerCantItems(request):

        cantidadItems = ({'items':request.session['items']})
        return HttpResponse(simplejson.dumps(cantidadItems), content_type='application/json')

