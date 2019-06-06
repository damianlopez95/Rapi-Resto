from django.contrib import admin
from .models import AlimentoCarta, Alimento, Carta, Sucursal, Opinion, Pedido, Categoria, Tipo, Mesa, AlimentoPedido
from .models import Usuario

admin.site.register(AlimentoCarta)
admin.site.register(Alimento)
admin.site.register(Carta)
admin.site.register(Sucursal)
admin.site.register(Opinion)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Tipo)
admin.site.register(Mesa)
admin.site.register(AlimentoPedido)

admin.site.register(Usuario)

