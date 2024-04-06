from django.shortcuts import render
from django.db.models import Sum, Count, DateField
from django.db.models.functions import TruncMonth
from .models import Venta, Cliente, Ubicacion

# Create your views here.
def ventas_por_mes(request):
    ventas = Venta.objects.annotate(
        mes=TruncMonth('fecha')
    ).values('mes').annotate(
        total_ventas=Sum('monto'),
        num_ventas=Count('id')
    ).order_by('mes')

    datos = [
        {'mes': venta['mes'].strftime('%B'), 'total_ventas': venta['total_ventas'], 'num_ventas': venta['num_ventas']}
        for venta in ventas
    ]

    return render(request, 'analisis_ventas/dashboard.html', {'ventas_por_mes': datos})

def ventas_por_ubicacion(request):
    ventas = Venta.objects.values('ubicacion__nombre', 'ubicacion__ciudad', 'ubicacion__pais').annotate(
        total_ventas=Sum('monto')
    ).order_by('-total_ventas')

    datos = [
        {'ubicacion': f"{venta['ubicacion__nombre']}, {venta['ubicacion__ciudad']}, {venta['ubicacion__pais']}",
         'total_ventas': venta['total_ventas']}
        for venta in ventas
    ]

    return render(request, 'analisis_ventas/dashboard.html', {'ventas_por_ubicacion': datos})