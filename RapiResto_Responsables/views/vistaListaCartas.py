from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from RapiResto_Responsables.forms import CartaIDForm, CartaForm
from RapiResto_Responsables.models import Carta

class VistaListaCarta(View) :

    def editar(request, pkcarta):

        carta = Carta.objects.get(pk=pkcarta)
        if request.method == 'POST':
            form = CartaForm(request.POST, request.FILES, instance=carta)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacartas')

        carta = Carta.objects.get(pk=pkcarta)
        form = CartaForm(instance=carta)
        return render(request,"editarcarta.html", {
        "form" : form
        })

    def obtenerCartas(request):

        if request.method == 'POST':
            form = CartaIDForm(request.POST)
            if form.is_valid():
                if 'editar' in request.POST:
                    return HttpResponseRedirect('editar/' + str(form.cleaned_data['carta']))
                elif 'eliminar' in request.POST:
                    carta = Carta.objects.get(pk = form.cleaned_data['carta'])
                    carta.delete()
                    return HttpResponseRedirect("/listacartas")

        form = CartaIDForm()
        permiso = request.user.groups.filter(name='GestorDeCartas').exists()
        cartas = Carta.objects.all()
        return render(request,"listaCartas.html", {
        "form" : form,
        "cartas" : cartas,
        "permiso" : permiso
     })

