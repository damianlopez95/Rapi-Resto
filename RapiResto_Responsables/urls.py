from django.urls import path

from .views import VistaAlimento, VistaLogin, VistaBienvenida

urlpatterns = [
    path('alimento', VistaAlimento.alimento_campos),
    path('loginuser', VistaLogin.loginUser, name = "loginuser"),
    path('logout', VistaLogin.logoutUser, name = "logout"),
    path('bienvenida', VistaBienvenida.comenzar, name = "bienvenida"),
]

