from django.urls import path

from .views import VistaCarta, VistaCartas, VistaSucursales, VistaCarrito

urlpatterns = [

    #URLs que sirven como selección de sucursal, cartas y alimentos
        #URL inicial de selección de sucursal y mesa
        path('', VistaSucursales.obtenerSucursales, name="sucursales"),
        path('obtenerMesas', VistaSucursales.obtenerMesas, name = "obtenerMesas"),
        path('<int:pksucursal>/cartas',VistaCartas.as_view(), name = "cartas"),
        path('carta/<int:pkcarta>', VistaCarta.obtenerAlimentos, name = "carta"),

    #URLs para operar con el carrito de compras
        path('carrito', VistaCarrito.obtenerCarrito, name = "carrito"),
        path('agregaritem', VistaCarrito.agregarItem, name = "agregaritem"),
        path('eliminarItem', VistaCarrito.eliminarItem, name = "eliminarItem"),
        path('confirmar', VistaCarrito.confirmarPedido, name = "confirmar"),
        path('obtenerItems', VistaCarrito.obtenerCantItems, name = "obtenerItems")
]
