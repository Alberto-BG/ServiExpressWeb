from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Servicio)
admin.site.register(TipoEmpleado)
admin.site.register(ResHora)
admin.site.register(Empleado)
admin.site.register(BolFac)
admin.site.register(Proveedor)
admin.site.register(OrdPedido)
admin.site.register(ProdServ)
admin.site.register(ProdProv)