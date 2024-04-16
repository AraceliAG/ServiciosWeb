import json
import datetime
import os
import pandas as pd

# Leer los datos del archivo CSV
data = pd.read_csv("datos_tonala_2.csv")

# Convertir la columna 'temperatura' a números y quitar el símbolo de grado
data['humedad'] = data['humedad'].str.replace('%', '').astype(int)

# Función para parsear las fechas
def custom_date_parser(date_string):
    parts = date_string.split(' ')
    months_es = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6, 'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12}
    date = datetime.datetime(int(parts[3]), months_es[parts[2]], int(parts[1]))
    return date

# Aplicar la función de parsing a la columna 'fecha'
data['fecha'] = data['fecha'].apply(custom_date_parser)

# Generar datos de la gráfica en el formato requerido por LightweightCharts
chartData = [{'time': date.strftime('%Y-%m-%d'), 'value': temp} for date, temp in zip(data['fecha'], data['humedad'])]

# LIT ES LA RUTA ACTUAL DEL ARCHIVO ACTUAL 
current_directory = os.path.dirname(os.path.abspath(__file__))

# RUTA DE JS CONSIDERANDO EN ESTE CASO EL ARCHIVO JS
js_file_path = os.path.join(current_directory, 'graficaH.js')

# VERIFICAMOS SI YA EXISTE EL ARCHIVO 
if os.path.exists(js_file_path):
    with open(js_file_path, 'r') as f:
        lines = f.readlines()
    
    # BUSCAMOS LA LINEA DEL var charData
    start_index = None
    for i, line in enumerate(lines):
        if 'var chartData =' in line:
            start_index = i
            break

    #SI SE ENCUENTRA REEMPLAZMOS POR LOS DATOS GENERADOS
    if start_index is not None:
        end_index = start_index
        while end_index < len(lines) and '];' not in lines[end_index]:
            end_index += 1
        del lines[start_index:end_index+1]

    # AQUI SE ESCRIBEN LOS DATO NUEVOS
    with open(js_file_path, 'w') as f:
        f.write("var chartData = ")
        json.dump(chartData, f)
        f.write(";\n")
        f.writelines(lines)
else:
    # SI NO  EXISTE EL ARCHIVO ACTUAL SE GENERA UN ARCHIVO NUEVO
    with open(js_file_path, 'w') as f:
        f.write("var chartData = ")
        json.dump(chartData, f)
        f.write(";\n")

