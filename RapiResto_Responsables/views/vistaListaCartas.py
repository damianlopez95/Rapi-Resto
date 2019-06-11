from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from RapiResto_Responsables.forms import CartaIDForm, CartaForm, AlimentoCartaIDForm, AlimentoCartaForm
from RapiResto_Responsables.models import Carta, AlimentoCarta, Alimento

class VistaListaCarta(View) :

    def crearCarta(request):

        if request.method == 'POST':
            form = CartaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacartas')

        form = CartaForm()
        print(form)
        return render(request,"creacionCarta.html", {
        "form" : form
        })

    def crearAlimentoCarta(request, pkcarta):

        if request.method == 'POST':
            form = AlimentoCartaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacarta/' + str(pkcarta))

        form = AlimentoCartaForm()
        carta = Carta.objects.get(pk = pkcarta)
        alimentos = Alimento.objects.all()
        return render(request,"creacionAlimentoCarta.html", {
        "form" : form,
        "carta" : carta,
        "alimentos" : alimentos
        })

    def editarAlimentoCarta(request, pkalimentocarta):

        alimentoCarta = AlimentoCarta.objects.get(pk=pkalimentocarta)
        if request.method == 'POST':
            form = AlimentoCartaForm(request.POST, request.FILES, instance=alimentoCarta)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacarta/' + str(alimentoCarta.carta.id))

        form = AlimentoCartaForm()
        carta = Carta.objects.get(pk = alimentoCarta.carta.id)
        return render(request,"editaralimentocarta.html", {
        "form" : form,
        "carta": carta,
        "alimentoCarta" : alimentoCarta
        })

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
        permiso = request.user.groups.filter(name='GestorDeCartas').exists()
        cartas = Carta.objects.all()
        return render(request,"listaCartas.html", {
        "form" : form,
        "cartas" : cartas,
        "permiso" : permiso
     })

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
        permisoGC = request.user.groups.filter(name='GestorDeCartas').exists()
        permisoR = request.user.groups.filter(name='Repositor').exists()
        return render(request, "listaCarta.html", {
            "form" : form,
            "carta" : carta,
            "alimentosCarta" : alimentosCarta,
            "permisoGC" : permisoGC,
            "permisoR"  : permisoR
        })
