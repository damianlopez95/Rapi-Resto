from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from RapiResto_Responsables.forms import CartaIDForm, CartaForm, AlimentoCartaIDForm, AlimentoCartaForm
from RapiResto_Responsables.models import Carta, AlimentoCarta, Alimento

class VistaListaCarta(View) :

    @login_required
    @permission_required('RapiResto_Responsables.add_carta')
    def crearCarta(request):

        if request.method == 'POST':
            form = CartaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacartas')

        print(request.user.get_all_permissions())
        form = CartaForm()
        print(form)
        return render(request,"creacionCarta.html", {
        "form" : form
        })

    @login_required
    @permission_required('RapiResto_Responsables.change_carta')
    def editarCarta(request, pkcarta):

        carta = Carta.objects.get(pk=pkcarta)
        if request.method == 'POST':
            form = CartaForm(request.POST, request.FILES, instance=carta)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacartas')

        form = CartaForm()
        return render(request,"editarcarta.html", {
        "form" : form,
        "carta" : carta
        })

    @login_required
    def obtenerCartas(request):

        if request.method == 'POST':
            form = CartaIDForm(request.POST)
            if form.is_valid():
                if 'editar' in request.POST:
                    return HttpResponseRedirect('/editarcarta/' + str(form.cleaned_data['carta']))
                elif 'eliminar' in request.POST:
                    carta = Carta.objects.get(pk = form.cleaned_data['carta'])
                    carta.delete()
                    return HttpResponseRedirect("/listacartas")

        form = CartaIDForm()
        permisos = {'GestorDeCartas' : request.user.groups.filter(name='GestorDeCartas').exists(),
                    'Superuser': request.user.is_superuser}
        print(permisos['GestorDeCartas'])
        cartas = Carta.objects.all()
        return render(request,"listaCartas.html", {
        "form" : form,
        "cartas" : cartas,
        "permisos" : permisos,
     })

    @login_required
    def obtenerCarta(request, pkcarta):
        
        if request.method == 'POST':
            form = AlimentoCartaIDForm(request.POST)
            if form.is_valid():
                if 'editar' in request.POST:
                    return HttpResponseRedirect('/editaralimentocarta/' + str(form.cleaned_data['alimentocarta']))
                elif 'eliminar' in request.POST:
                    alimentoCarta = AlimentoCarta.objects.get(pk = form.cleaned_data['alimentocarta'])
                    pk = alimentoCarta.carta.id
                    alimentoCarta.delete()
                    return HttpResponseRedirect("/listacarta/" + str(pk))

        form = AlimentoCartaIDForm()
        carta = Carta.objects.get(pk = pkcarta)
        alimentosCarta = AlimentoCarta.objects.filter(carta = pkcarta)
        permisos = {'GestorDeCartas' : request.user.groups.filter(name='GestorDeCartas').exists(),
                    'Repositor': request.user.groups.filter(name='Repositor').exists(),
                    'Superuser': request.user.is_superuser}
        return render(request, "listaCarta.html", {
            "form" : form,
            "carta" : carta,
            "alimentosCarta" : alimentosCarta,
            "permisos" : permisos,
        })

