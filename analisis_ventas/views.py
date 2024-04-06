from django.shortcuts import render
from .models import Venta
import pandas as pd

def index(request):
    # Preparar datos de ventas por mes
    ventas_qs = Venta.objects.all()
    ventas_df = pd.DataFrame(list(ventas_qs.values('fecha', 'monto')))
    ventas_df['fecha'] = pd.to_datetime(ventas_df['fecha'])
    ventas_por_mes = ventas_df.resample('M', on='fecha').monto.sum().reset_index()
    meses = ventas_por_mes['fecha'].dt.strftime('%Y-%m').tolist()
    montos = ventas_por_mes['monto'].tolist()

    # Aquí puedes añadir más lógica para preparar otros datos, como ventas por ubicación

    # Pasar todos los datos procesados a la plantilla
    context = {
        'meses': meses,
        'montos': montos,
        # Añadir más datos al contexto según sea necesario
    }
    return render(request, 'analisis_ventas/index.html', context)