from django.db.models.functions import TruncMonth
from django.db.models import Sum
from django.shortcuts import render
from analisis_ventas.models import Venta
import pandas as pd

def reporte(request):
    # Preparar datos de ventas por mes
    ventas_qs = Venta.objects.all()
   
    context = {
        'ventas_qs':ventas_qs,
    }
    return render(request, 'analisis_ventas/index.html', context)