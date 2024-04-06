from django.contrib import admin
from .models import Venta, Cliente, Ubicacion

# Register your models here.
# class VentasAdmin(admin.ModelAdmin):
#    list_display = ('id', 'fecha', 'monto', 'cliente', 'ubicacion')
#    list_filter = ('fecha', 'cliente', 'ubicacion')

# Register your models here.
admin.site.register(Venta)
admin.site.register(Cliente)
admin.site.register(Ubicacion)
