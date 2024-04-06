from django.contrib import admin
from analisis_ventas.models import Venta

# https://docs.djangoproject.com/en/5.0/ref/contrib/admin/
# Register your models here.
class VentasAdmin(admin.ModelAdmin):
    list_display = ["fecha", "monto", "nombre_cliente", "email_cliente", "locacion", "ciudad", "pais"]
    search_fields = ["nombre_cliente", "email_cliente", "ciudad", "pais"]  # Permite buscar por estos campos
    list_filter = ["fecha", "ciudad", "pais"]  # Permite filtrar por estos campos en la barra lateral


# Register your models here.
admin.site.register(Venta, VentasAdmin)