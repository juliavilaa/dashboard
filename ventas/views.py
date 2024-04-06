from django.shortcuts import render
from ventas.models import Venta
import plotly.express as px
import pandas as pd
import numpy as np

def saludar(request):
    if request.user.is_authenticated:
        nombre_usuario = request.user.username
    else:
        nombre_usuario = "Usuario desconocido"  


    ventas = Venta.objects.all()
    data={
     'Barrio': ['Barrio A', 'Barrio B', 'Barrio C', 'Barrio A', 'Barrio B', 'Barrio C'],
        'Mes': ['Enero', 'Enero', 'Enero', 'Febrero', 'Febrero', 'Febrero'],
        'Ventas': np.random.randint(100, 1000, 6)  # Ventas aleatorias para cada barrio y mes
        }
    df=pd.DataFrame(data)
    grafica=px.bar(df, x='Mes', y='Ventas', color='Barrio', barmode='group', title='Ventas por Mes y Barrio')
    mihtml=grafica.to_html(full_html=False)
    context = {
        "nombre": nombre_usuario,  
        "ventas": ventas,
        "grafica":mihtml
        }
    return render(request,"ventas/index.html",context)
