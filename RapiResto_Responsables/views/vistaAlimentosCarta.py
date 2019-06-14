from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from RapiResto_Responsables.forms import  AlimentoCartaForm
from RapiResto_Responsables.models import Carta, AlimentoCarta, Alimento

class VistaAlimentoCarta(View) :

    @login_required
    @permission_required('RapiResto_Responsables.add_alimentocarta')
    def crearAlimentoCarta(request, pkcarta):

        if request.method == 'POST':
            form = AlimentoCartaForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/listacarta' + str(pkcarta))

        form = AlimentoCartaForm()
        carta = Carta.objects.get(pk = pkcarta)
        alimentos = Alimento.objects.all()
        return render(request,"creacionAlimentoCarta.html", {
        "form" : form,
        "carta" : carta,
        "alimentos" : alimentos
        })

    @login_required
    @permission_required('RapiResto_Responsables.change_alimentocarta')
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

