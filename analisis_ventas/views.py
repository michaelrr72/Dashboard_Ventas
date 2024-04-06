from django.shortcuts import render
from analisis_ventas.models import Venta
import pandas as pd
import plotly.express as px

def reporte(request):
    
    ventas_qs = Venta.objects.all().values("fecha", "monto", "nombre_cliente", "email_cliente", "locacion", "ciudad", "pais")
    df = pd.DataFrame(list(ventas_qs))
    
    grafico = px.bar(df, x="ciudad", y="monto", color="pais")
    miHtml = grafico.to_html(full_html = False)
   
    context = {
        'ventas_qs':ventas_qs,
        'grafica':miHtml,
    }
    return render(request, 'analisis_ventas/index.html', context)