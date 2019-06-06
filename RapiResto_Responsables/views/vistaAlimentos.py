from django.shortcuts import render
from django.views.generic import View

from RapiResto_Responsables.forms import AlimentoForm
from RapiResto_Responsables.models import Alimento

class VistaAlimento(View) :

    def alimento_campos(request):

        if request.method == 'POST':
            form = AlimentoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

        form = AlimentoForm()
        return render(request,"alimento.html", {
        "form" : form
     })

