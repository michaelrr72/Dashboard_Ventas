from django.db import models

# Create your models here.
class Venta(models.Model):
    fecha = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='ventas')
    ubicacion = models.ForeignKey('Ubicacion', on_delete=models.CASCADE, related_name='ventas')
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)