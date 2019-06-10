from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect

from RapiResto_Responsables.forms import AlimentoForm, AlimentoIDForm
from RapiResto_Responsables.models import Alimento

class VistaAlimento(View) :

    def crearAlimento(request):

        if request.method == 'POST':
            form = AlimentoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        form = AlimentoForm()
        return render(request,"alimento.html", {
        "form" : form
     })

    def verAlimento(request, pkalimento):

        alimento = Alimento.objects.get(pk=pkalimento)
        return render(request,"verAlimento.html", {
            "alimento" : alimento
        })

    def obtenerAlimentos(request):

        if request.method == 'POST':
            form = AlimentoIDForm(request.POST)
            if form.is_valid():
                if 'editar' in request.POST:
                    return HttpResponseRedirect('/editaralimento/' + str(form.cleaned_data['alimento']))
                elif 'eliminar' in request.POST:
                    alimento = Alimento.objects.get(pk = form.cleaned_data['carta'])
                    alimento.delete()
                    return HttpResponseRedirect("/listacartas")

        form = AlimentoIDForm()
        permiso = request.user.groups.filter(name='GestorDeAlimentos').exists()
        alimentos = Alimento.objects.all()
        return render(request,"listaAlimentos.html", {
        "form" : form,
        "alimentos" : alimentos,
        "permiso" : permiso
     })
