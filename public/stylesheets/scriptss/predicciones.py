from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily

# Establecer periodo de tiempo
inicio = datetime(2015, 1, 12)
fin = datetime(2023, 12, 31)

# Crear punto para Jalisco
tonala = Point(20.6667, -103.3833, 1570)

# Get daily data for 2018
data = Daily(tonala, inicio, fin)
data = data.fetch()
print(data) #TODO BIEN ACA SOLO IMPRIME LOS PARAMETROS JUNTO A LA FECHA