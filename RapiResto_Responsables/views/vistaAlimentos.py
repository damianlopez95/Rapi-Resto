from django.shortcuts import render
from django.views.generic import View
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from RapiResto_Responsables.forms import AlimentoForm, AlimentoIDForm
from RapiResto_Responsables.models import Alimento, Categoria

class VistaAlimento(View) :

    @login_required
    @permission_required('RapiResto_Responsables.add_alimento')
    def crearAlimento(request):

        if request.method == 'POST':
            form = AlimentoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/listaalimentos")

        form = AlimentoForm()
        alimentos = Alimento.objects.all()
        categorias = Categoria.objects.all()
        return render(request,"creacionAlimento.html", {
        "form" : form,
        "alimentos" : alimentos,
        "categorias" : categorias
     })

    @login_required
    @permission_required('RapiResto_Responsables.change_alimento')
    def editarAlimento(request, pkalimento):

        alimento = Alimento.objects.get(pk = pkalimento)
        if request.method == 'POST':
            form = AlimentoForm(request.POST, request.FILES, instance=alimento)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/listaalimentos")

        form = AlimentoForm()
        alimentos = Alimento.objects.filter(~Q(pk = pkalimento))
        for recomendacion in alimento.recomendaciones.all():
            if recomendacion in alimentos:
                alimentos = alimentos.exclude(id=recomendacion.id)
        categorias = Categoria.objects.all()
        return render(request,"editarAlimento.html", {
        "form" : form,
        "alimento" : alimento,
        "alimentos" : alimentos,
        "categorias" : categorias
     })

    @login_required
    def verAlimento(request, pkalimento):

        alimento = Alimento.objects.get(pk=pkalimento)
        return render(request,"verAlimento.html", {
            "alimento" : alimento
        })

    @login_required
    def obtenerAlimentos(request):

        if request.method == 'POST':
            form = AlimentoIDForm(request.POST)
            if form.is_valid():
                if 'editar' in request.POST:
                    return HttpResponseRedirect('/editaralimento/' + str(form.cleaned_data['alimento']))
                elif 'eliminar' in request.POST:
                    alimento = Alimento.objects.get(pk = form.cleaned_data['alimento'])
                    alimento.delete()
                    return HttpResponseRedirect("/listaalimentos")

        form = AlimentoIDForm()
        permiso = request.user.groups.filter(name='GestorDeAlimentos').exists() | request.user.is_superuser
        alimentos = Alimento.objects.all()
        return render(request,"listaAlimentos.html", {
        "form" : form,
        "alimentos" : alimentos,
        "permiso" : permiso
     })
