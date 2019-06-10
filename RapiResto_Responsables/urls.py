from django.urls import path

from .views import VistaAlimento, VistaLogin, VistaBienvenida, VistaListaCarta

urlpatterns = [
    path('alimento', VistaAlimento.alimento_campos),
    path('loginuser', VistaLogin.loginUser, name = "loginuser"),
    path('logout', VistaLogin.logoutUser, name = "logout"),
    path('bienvenida', VistaBienvenida.comenzar, name = "bienvenida"),
    path('listacartas', VistaListaCarta.obtenerCartas, name = "listacartas"),
    path('editar/<int:pkcarta>', VistaListaCarta.editar, name = "editar"),
]

