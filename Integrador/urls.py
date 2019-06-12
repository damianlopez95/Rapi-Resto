from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("RapiResto_Clientes.urls")),
    path('', include("RapiResto_Responsables.urls")),
    url(r'^notifications/', include('notify.urls', 'notifications')),
]
