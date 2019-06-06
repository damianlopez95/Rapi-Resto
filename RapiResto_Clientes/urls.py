from django.urls import path

from .views import VistaCarta, VistaCartas, VistaSucursales, VistaCarrito

urlpatterns = [
    path('cartas/<int:pksucursal>',VistaCartas.as_view(), name = "cartas"),
    path('carta/<int:pkcarta>', VistaCarta.getAlimento, name = "carta"),
    path('sucursales', VistaSucursales.getSucursales, name = "sucursales"),
    path('getMesas', VistaSucursales.getMesas, name = "getMesas"),
    path('carrito', VistaCarrito.getCarrito, name = "carrito"),
    path('delete', VistaCarrito.delete, name = "delete"),
    path('confirmar', VistaCarrito.confPedido, name = "confirmar")
]
