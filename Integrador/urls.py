from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("RapiResto_Clientes.urls")),
    path('', include("RapiResto_Responsables.urls"))
]
