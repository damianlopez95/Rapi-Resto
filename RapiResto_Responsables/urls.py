from django.urls import path

from .views import VistaAlimento, VistaLogin, VistaBienvenida, VistaListaCarta, VistaPedido

urlpatterns = [
    #URLs de login y logout
        path('loginuser', VistaLogin.loginUser, name = "loginuser"),
        path('logout', VistaLogin.logoutUser, name = "logout"),

    #URL de bienvenida a app de gestión
        path('bienvenida', VistaBienvenida.comenzar, name = "bienvenida"),

    #URLs de creación de elementos
        path('crearalimento', VistaAlimento.crearAlimento, name = "crearalimento"),
        path('crearcarta', VistaListaCarta.crearCarta, name = "crearcarta"),
        path('crearalimentocarta/<int:pkcarta>', VistaListaCarta.crearAlimentoCarta, name = "crearalimentocarta"),

    #URLs de edición de elementos
        path('editarcarta/<int:pkcarta>', VistaListaCarta.editarCarta, name = "editarcarta"),
        path('editaralimentocarta/<int:pkalimentocarta>', VistaListaCarta.editarAlimentoCarta, name = "editaralimentocarta"),
        path('editaralimento/<int:pkalimento>', VistaAlimento.editarAlimento, name = "editaralimento"),

    #URLs de petición de listas de elementos
        path('listacartas', VistaListaCarta.obtenerCartas, name = "listacartas"),
        path('listacarta/<int:pkcarta>', VistaListaCarta.obtenerCarta, name = "listacarta"),
        path('listaalimentos', VistaAlimento.obtenerAlimentos, name = "listaalimentos"),
        path('listapedidos', VistaPedido.obtenerPedidos, name = "listapedidos"),

    #URLs de petición de detalles de elementos
        path('veralimento/<int:pkalimento>', VistaAlimento.verAlimento, name = "veralimento"),
        path('verpedido/<int:pkpedido>', VistaPedido.verPedido, name = "verpedido"),
]

