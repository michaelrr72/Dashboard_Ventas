from django.shortcuts import render
from django.db.models import Sum, Count, DateField
from django.db.models.functions import TruncMonth
from .models import Venta, Cliente, Ubicacion
import plotly.graph_objs as go

# Create your views here.
def ventas_por_mes(request):
    ventas = Venta.objects.annotate(
        mes=TruncMonth('fecha')
    ).values('mes').annotate(
        total_ventas=Sum('monto'),
        num_ventas=Count('id')
    ).order_by('mes')
    
    # Crear la figura de Plotly
    data = [go.Bar(x=[venta['mes'] for venta in ventas], y=[venta['total_ventas'] for venta in ventas])]
    layout = go.Layout(title='Ventas por Mes', xaxis_title='Mes', yaxis_title='Total de Ventas')
    figura = go.Figure(data=data, layout=layout)

    # Convertir la figura a JSON
    figura_json = figura.to_json()

    # Renderizar la plantilla y pasar los datos como contexto
    return render(request, 'analisis_ventas/dashboard.html', {'ventas_por_mes_json': figura_json})

def ventas_por_ubicacion(request):
    ventas = Venta.objects.values('ubicacion__nombre', 'ubicacion__ciudad', 'ubicacion__pais').annotate(
        total_ventas=Sum('monto')
    ).order_by('-total_ventas')

    # Crear la figura de Plotly
    data = [go.Bar(x=[venta['ubicacion'] for venta in ventas], y=[venta['total_ventas'] for venta in ventas])]
    layout = go.Layout(title='Ventas por Ubicación', xaxis_title='Ubicación', yaxis_title='Total de Ventas')
    figura = go.Figure(data=data, layout=layout)

    # Convertir la figura a JSON
    figura_json = figura.to_json()

    # Renderizar la plantilla y pasar los datos como contexto
    return render(request, 'analisis_ventas/dashboard.html', {'ventas_por_ubicacion_json': figura_json})