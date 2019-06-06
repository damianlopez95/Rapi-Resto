from django.urls import path

from .views import VistaAlimento, VistaLogin

urlpatterns = [
    path('alimento', VistaAlimento.alimento_campos),
    path('loginuser', VistaLogin.loginUser, name = "loginuser"),
    path('logout', VistaLogin.logoutUser, name = "logout")
]

