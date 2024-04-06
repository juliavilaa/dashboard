# Dashboard de Ventas con Django y Plotly

Este proyecto consiste en un dashboard interactivo que muestra las ventas de una compañía, analizando datos como la ubicación de los compradores por barrios y las ventas por cada mes del año. Utiliza Django para el backend, SQLite como base de datos, y Plotly junto con Bootstrap y jQuery para el frontend.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias utilizando pip:
pip install -r requirements.txt
3. Ejecuta el servidor Django:
python manage.py runserver

4. Abre tu navegador web y visita `http://localhost:8000/ventas/` para ver el dashboard de ventas.

## Estructura del Proyecto

- `dashboard/`: Directorio raíz del proyecto Django.
- `ventas/`: Aplicación Django que contiene las vistas, modelos y templates para el dashboard de ventas.
  - `models.py`: Definición del modelo `Venta`.
  - `views.py`: Implementación de las vistas, incluyendo la vista `saludar` que muestra el dashboard.
  - `urls.py`: Configuración de las URL para el proyecto.
  - `templates/ventas/index.html`: Template HTML para el dashboard.
- `README.md`: Este archivo que estás leyendo ahora.

## Tecnologías Utilizadas

- Python 3
- Django
- SQLite
- Plotly
- Bootstrap
- jQuery
