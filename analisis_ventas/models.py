from django.db import models

# Create your models here.
class Venta(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_cliente = models.CharField(max_length=120)
    email_cliente = models.EmailField(unique=True)
    locacion = models.CharField(max_length=120)
    ciudad = models.CharField(max_length=120)
    pais = models.CharField(max_length=120)