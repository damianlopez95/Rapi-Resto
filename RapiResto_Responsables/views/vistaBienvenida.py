from django.shortcuts import render
from django.views.generic import View

class VistaBienvenida(View) :

    def comenzar(request):

        return render(request, 'bienvenida.html', {})

