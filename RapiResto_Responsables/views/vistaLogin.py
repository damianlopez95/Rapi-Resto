from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout
from django.contrib import messages

from RapiResto_Responsables.forms import LoginForm

class VistaLogin(View) :

    def loginUser(request):

        if request.method == 'POST':
            form = LoginForm(data = request.POST)
            if form.is_valid():
                usuario = form.get_user()
                login(request, usuario)
                return redirect('bienvenida')
        else:
            form = LoginForm()

        if request.user.is_authenticated:
            return redirect('bienvenida')
        else:
            return render(request,"login.html", {'form' : form})

    def logoutUser(request):

        logout(request)
        return redirect('/loginuser')

