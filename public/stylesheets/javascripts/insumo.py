import pandas as pd

# Cargar datos desde el archivo CSV
data = pd.read_csv("datos_tonala_2.csv")

# Visualizar los primeros 5 registros
print("Primeros 5 registros:")
print(data.head())

# Visualizar los últimos 5 registros
print("\nÚltimos 5 registros:")
print(data.tail())

# Visualizar la información general del DataFrame
print("\nInformación general:")
print(data.info())

