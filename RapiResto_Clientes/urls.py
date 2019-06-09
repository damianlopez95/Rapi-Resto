from django.urls import path

from .views import VistaCarta, VistaCartas, VistaSucursales, VistaCarrito

urlpatterns = [
    path('', VistaSucursales.getSucursales, name="sucursales"),
    path('cartas/<int:pksucursal>',VistaCartas.as_view(), name = "cartas"),
    path('carta/<int:pkcarta>', VistaCarta.getAlimento, name = "carta"),
    path('getMesas', VistaSucursales.getMesas, name = "getMesas"),
    path('getItems', VistaCarrito.getItems, name = "getItems"),
    path('carrito', VistaCarrito.getCarrito, name = "carrito"),
    path('delete', VistaCarrito.delete, name = "delete"),
    path('confirmar', VistaCarrito.confPedido, name = "confirmar")
]
