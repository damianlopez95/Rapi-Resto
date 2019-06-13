from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class VistaBienvenida(View) :

    @login_required
    def comenzar(request):

        return render(request, 'bienvenida.html', {})

