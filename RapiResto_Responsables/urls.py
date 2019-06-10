from django.urls import path

from .views import VistaAlimento, VistaLogin, VistaBienvenida, VistaListaCarta, VistaPedido

urlpatterns = [
    path('crearalimento', VistaAlimento.crearAlimento, name = "crearalimento"),
    path('loginuser', VistaLogin.loginUser, name = "loginuser"),
    path('logout', VistaLogin.logoutUser, name = "logout"),
    path('bienvenida', VistaBienvenida.comenzar, name = "bienvenida"),
    path('listacartas', VistaListaCarta.obtenerCartas, name = "listacartas"),
    path('listacarta/<int:pkcarta>', VistaListaCarta.obtenerCarta, name = "listacarta"),
    path('editarcarta/<int:pkcarta>', VistaListaCarta.editarCarta, name = "editarcarta"),
    path('editaralimentocarta/<int:pkalimentocarta>', VistaListaCarta.editarAlimentoCarta, name = "editaralimentocarta"),
    path('crearcarta', VistaListaCarta.crearCarta, name = "crearcarta"),
    path('crearalimentocarta/<int:pkcarta>', VistaListaCarta.crearAlimentoCarta, name = "crearalimentocarta"),
    path('veralimento/<int:pkalimento>', VistaAlimento.verAlimento, name = "veralimento"),
    path('listaalimentos', VistaAlimento.obtenerAlimentos, name = "listaalimentos"),
    path('listapedidos', VistaPedido.obtenerPedidos, name = "listapedidos"),
    path('verpedido/<int:pkpedido>', VistaPedido.verPedido, name = "verpedido"),
]

