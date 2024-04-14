import json
import datetime
import os

import pandas as pd

# Leer los datos del archivo CSV
data = pd.read_csv("datos_tonala_2.csv")

# Convertir la columna 'temperatura' a números y quitar el símbolo de grado
data['temperatura'] = data['temperatura'].str.replace('°', '').astype(int)

# Función para parsear las fechas
def custom_date_parser(date_string):
    parts = date_string.split(' ')
    months_es = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    date = datetime.datetime(int(parts[3]), months_es[parts[2]], int(parts[1]))
    return date

# Aplicar la función de parsing a la columna 'fecha'
data['fecha'] = data['fecha'].apply(custom_date_parser)

# Generar datos de la gráfica en el formato requerido por LightweightCharts
charData = [{'time': date.strftime('%Y-%m-%d'), 'value': temp} for date, temp in zip(data['fecha'], data['temperatura'])]

# Verificar si el archivo JavaScript existe y contiene datos
if os.path.exists('grafica4.js') and os.path.getsize('grafica4.js') > 0:
    # LEER EL CONTENIDO ACTUAL DEL ARCHIVO JAVASCRIPT
    with open('grafica4.js', 'r') as f:
        existing_code = f.read()

    # ABRIR EL ARCHIVO JAVASCRIPT EN MODO ESCRITURA Y SOBRESCRIBIR EL NUEVO CODIGO
    with open('grafica4.js', 'w') as f:
        f.write("var charData = ")
        json.dump(charData, f)
        f.write(";\n")
        f.write(existing_code)
else:
    # Escribir los datos en un nuevo archivo JavaScript
    with open('grafica4.js', 'w') as f:
        f.write("var chart_data = ")
        json.dump(charData, f)
        f.write(";\n")
