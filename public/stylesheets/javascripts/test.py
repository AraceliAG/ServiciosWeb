import pandas as pd
import json
import datetime

data = pd.read_csv("datos_tonala_2.csv")

#CONVERSION A INT
# Temperatura a números y quitar el °
data['temperatura'] = data['temperatura'].str.replace('°', '').astype(int)

# FUNCION 
def custom_date_parser(date_string):
    # Dividir la cadena en: día de la semana, día, mes, año
    parts = date_string.split(' ')
    # Mapear nombres de los meses en español a números de mes
    months_es = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    # Crear un objeto datetime
    date = datetime.datetime(int(parts[3]), months_es[parts[2]], int(parts[1]))
    return date

data['fecha'] = data['fecha'].apply(custom_date_parser)

# Generar datos de la gráfica en el formato requerido por LightweightCharts
chart_data = [{'time': date.strftime('%Y-%m-%d'), 'value': temp} for date, temp in zip(data['fecha'], data['temperatura'])]

# Escribir los datos en un archivo JavaScript (modo append)
with open('grafica3.js', 'a') as f:
    f.write("\nvar chart_data = ")
    json.dump(chart_data, f)
    f.write(";\n")
