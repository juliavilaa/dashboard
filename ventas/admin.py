from django.contrib import admin
from ventas.models import Venta
class VentasAdmin(admin.ModelAdmin):
    list_display=["barrio","mes"]

admin.site.register(Venta,VentasAdmin)
