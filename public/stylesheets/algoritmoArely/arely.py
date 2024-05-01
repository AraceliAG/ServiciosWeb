from datetime import datetime
import matplotlib.pyplot as plt
from meteostat import Point, Daily
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
import seaborn as sns

# Establecer periodo de tiempo
inicio = datetime(2015, 1, 12)
fin = datetime(2023, 12, 31)

# Crear punto para Jalisco
tonala = Point(20.6667, -103.3833, 1570)

# Get daily data for 2018
data = Daily(tonala, inicio, fin)
data = data.fetch()
#print(data) #TODO BIEN ACA SOLO IMPRIME LOS PARAMETROS JUNTO A LA FECHA
# print(data.head()) #TODO BIEN LAS CABECERAS
data.head()



def uno ():
    data.to_csv('2018-2023.csv', index=True) # Para guardar sin el índice del DataFrame

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 20.6244,
	"longitude": -103.2342,
	"start_date": "2000-01-01",
	"end_date": "2009-12-31",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(3).ValuesAsNumpy()
daily_rain_sum = daily.Variables(4).ValuesAsNumpy()
daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()
daily_precipitation_hours = daily.Variables(6).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(7).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["rain_sum"] = daily_rain_sum
daily_data["snowfall_sum"] = daily_snowfall_sum
daily_data["precipitation_hours"] = daily_precipitation_hours
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max

daily_dataframe_10 = pd.DataFrame(data = daily_data)
print(daily_dataframe_10)

def dos ():
    daily_dataframe_10.to_csv('2000 - 2010 - APIH2.csv', index=True) # Para guardar sin el índice del DataFrame
    # Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 20.6244,
	"longitude": -103.2342,
	"start_date": "2010-01-01",
	"end_date": "2019-12-31",
	"daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_sum", "rain_sum", "snowfall_sum", "precipitation_hours", "wind_speed_10m_max"]
}
responses = openmeteo.weather_api(url, params=params)

# Process first location. Add a for-loop for multiple locations or weather models
response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
daily_temperature_2m_mean = daily.Variables(2).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(3).ValuesAsNumpy()
daily_rain_sum = daily.Variables(4).ValuesAsNumpy()
daily_snowfall_sum = daily.Variables(5).ValuesAsNumpy()
daily_precipitation_hours = daily.Variables(6).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(7).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_max"] = daily_temperature_2m_max
daily_data["temperature_2m_min"] = daily_temperature_2m_min
daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["rain_sum"] = daily_rain_sum
daily_data["snowfall_sum"] = daily_snowfall_sum
daily_data["precipitation_hours"] = daily_precipitation_hours
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)



#FUNCION Dataset para predicciones
def tres():
    daily_dataframe.to_csv('2010 - 2022 - APIH.csv', index=True) # Para guardar sin el índice del DataFrame
    df_2000_2010 = pd.read_csv('2000 - 2010 - APIH.csv')
    df_2010_2022 = pd.read_csv('2010 - 2022 - APIH.csv')
    df_2000_2010.head()
    df_2010_2022.head()
    # Concatenar los DataFrames
    dfs = [df_2000_2010, df_2010_2022] # Concatenar los DataFrames
    df_historica = pd.concat(dfs, ignore_index=True)
    df_historica = df_historica.drop(columns=['Unnamed: 0'])# Eliminar columnas que no sirven
    # Cambiar nombre de columnas
    new_columns = ['fecha', 'temp_max', 'temp_min', 'temp_prom', 'precp', 'lluvia', 'nieve', 'precp_h', 'viento']

    # Asignar los nuevos nombres de columnas
    df_historica.columns = new_columns
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'], errors='coerce')

    # Extraer solo el año, mes y día de la columna de fecha
    df_historica['fecha'] = df_historica['fecha'].dt.date
    # Convertir la columna de fecha de nuevo a tipo datetime
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'])
    print("RESLTADO FINAL: ")
    print(df_historica.head()) #MUESTRA RESULTADO FINAL
    # Verificar si hay valores nulos
    nulos_totales = df_historica.isnull().sum()
    print(nulos_totales)
    registros_por_año = df_historica.groupby(df_historica['fecha'].dt.year).size()
    print(registros_por_año)
    # Establecer la columna de fecha como el índice del DataFrame
    df_historica = df_historica.set_index('fecha')
    df_historica.info()
    
    df_historica["temp_max"].plot()
    df_historica["temp_min"].plot()
    plt.show()
    
#Machine Learning - Predecir la temperatura futura
def cuatro():
    daily_dataframe.to_csv('2010 - 2022 - APIH.csv', index=True) # Para guardar sin el índice del DataFrame
    df_2000_2010 = pd.read_csv('2000 - 2010 - APIH.csv')
    df_2010_2022 = pd.read_csv('2010 - 2022 - APIH.csv')
    df_2000_2010.head()
    df_2010_2022.head()
    # Concatenar los DataFrames
    dfs = [df_2000_2010, df_2010_2022] # Concatenar los DataFrames
    df_historica = pd.concat(dfs, ignore_index=True)
    df_historica = df_historica.drop(columns=['Unnamed: 0'])# Eliminar columnas que no sirven
    # Cambiar nombre de columnas
    new_columns = ['fecha', 'temp_max', 'temp_min', 'temp_prom', 'precp', 'lluvia', 'nieve', 'precp_h', 'viento']

    # Asignar los nuevos nombres de columnas
    df_historica.columns = new_columns
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'], errors='coerce')

    # Extraer solo el año, mes y día de la columna de fecha
    df_historica['fecha'] = df_historica['fecha'].dt.date
    # Convertir la columna de fecha de nuevo a tipo datetime
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'])
    #print("RESLTADO FINAL: ")
    #print(df_historica.head()) #MUESTRA RESULTADO FINAL
    # Verificar si hay valores nulos
    nulos_totales = df_historica.isnull().sum()
    #print(nulos_totales)
    registros_por_año = df_historica.groupby(df_historica['fecha'].dt.year).size()
    #print(registros_por_año)
    # Establecer la columna de fecha como el índice del DataFrame
    df_historica = df_historica.set_index('fecha')
    #df_historica.info()
    
    df_historica["target"] = df_historica.shift(-1)["temp_max"]
    df_historica = df_historica.ffill() # Solucionar el target de la ultima fecha
    
    #print(df_historica)
    
    # Encontrar correlaciones
    #print(df_historica.corr())
    
    rr = Ridge(alpha=.1)
    predictors = df_historica.columns[~df_historica.columns.isin(["target"])]
    #print(predictors)
    def backtest(df_historica, model, predictors, start=3654, step=90):
        all_predictions = []

        for i in range(start, df_historica.shape[0], step):
            train = df_historica.iloc[:i,:]
            test = df_historica.iloc[i:(i+step),:]

            model.fit(train[predictors], train["target"])

            preds = model.predict(test[predictors])

            preds = pd.Series(preds, index=test.index)
            combined = pd.concat([test["target"], preds], axis=1)

            combined.columns = ["actual", "prediction"]
            combined["diff"] = (combined["prediction"] - combined["actual"]).abs()

            all_predictions.append(combined)

        return pd.concat(all_predictions)
    predictions = backtest(df_historica, rr, predictors)
    print("RESULTADO: ")
    #print(predictions)
    # print(mean_absolute_error(predictions["actual"], predictions["prediction"])) #En promedio predice 0.9439700364843344 grados de más o menos (lo cuál no está tan mal, de hecho está muy bien)
    # print(predictions.sort_values("diff", ascending=False))
    # print(df_historica.loc["2011-06-20":"2011-06-30"])
    # print(predictions["diff"].round().value_counts().sort_index())
    # predictions["diff"].round().value_counts().sort_index().plot()
    # plt.show()#muestra grafica
    # plt.figure(figsize=(10, 6))
    # plt.plot(predictions.index, predictions['actual'], label='Valores reales', color='blue')
    # plt.plot(predictions.index, predictions['prediction'], label='Predicciones', color='red')

    # plt.xlabel('Fecha')
    # plt.ylabel('Valor')
    # plt.title('Comparación de predicciones y valores reales')
    # plt.legend()

    # plt.show()#aqui muestra las graficas del los datos procesados y de las predicciones
    # sns.set_style("whitegrid")
    # plt.figure(figsize=(10, 6))
    # sns.lineplot(data=predictions, palette=["blue", "red"])

    # plt.xlabel('Fecha')
    # plt.ylabel('Valor')
    # plt.title('Comparación de predicciones y valores reales')

    # plt.show()#comparacion 
def calculadora():
    daily_dataframe.to_csv('2010 - 2022 - APIH.csv', index=True) # Para guardar sin el índice del DataFrame
    df_2000_2010 = pd.read_csv('2000 - 2010 - APIH.csv')
    df_2010_2022 = pd.read_csv('2010 - 2022 - APIH.csv')
    df_2000_2010.head()
    df_2010_2022.head()
    # Concatenar los DataFrames
    dfs = [df_2000_2010, df_2010_2022] # Concatenar los DataFrames
    df_historica = pd.concat(dfs, ignore_index=True)
    df_historica = df_historica.drop(columns=['Unnamed: 0'])# Eliminar columnas que no sirven
    # Cambiar nombre de columnas
    new_columns = ['fecha', 'temp_max', 'temp_min', 'temp_prom', 'precp', 'lluvia', 'nieve', 'precp_h', 'viento']

    # Asignar los nuevos nombres de columnas
    df_historica.columns = new_columns
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'], errors='coerce')

    # Extraer solo el año, mes y día de la columna de fecha
    df_historica['fecha'] = df_historica['fecha'].dt.date
    # Convertir la columna de fecha de nuevo a tipo datetime
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'])
    #print("RESLTADO FINAL: ")
    #print(df_historica.head()) #MUESTRA RESULTADO FINAL
    # Verificar si hay valores nulos
    nulos_totales = df_historica.isnull().sum()
    #print(nulos_totales)
    registros_por_año = df_historica.groupby(df_historica['fecha'].dt.year).size()
    #print(registros_por_año)
    # Establecer la columna de fecha como el índice del DataFrame
    df_historica = df_historica.set_index('fecha')
    #df_historica.info()
    
    df_historica["target"] = df_historica.shift(-1)["temp_max"]
    df_historica = df_historica.ffill() # Solucionar el target de la ultima fecha
    
    #print(df_historica)
    
    # Encontrar correlaciones
    #print(df_historica.corr())
    
    rr = Ridge(alpha=.1)
    predictors = df_historica.columns[~df_historica.columns.isin(["target"])]
    #print(predictors)
    def backtest(df_historica, model, predictors, start=3654, step=90):
        all_predictions = []

        for i in range(start, df_historica.shape[0], step):
            train = df_historica.iloc[:i,:]
            test = df_historica.iloc[i:(i+step),:]

            model.fit(train[predictors], train["target"])

            preds = model.predict(test[predictors])

            preds = pd.Series(preds, index=test.index)
            combined = pd.concat([test["target"], preds], axis=1)

            combined.columns = ["actual", "prediction"]
            combined["diff"] = (combined["prediction"] - combined["actual"]).abs()

            all_predictions.append(combined)

        return pd.concat(all_predictions)
    predictions = backtest(df_historica, rr, predictors)
    print("RESULTADO: ")

    valores_caracteristicas = {'temp_max': 25.613500, 'temp_min': 16.613500, 'temp_prom': 21.290585, 'precp': 2.90000, 'lluvia':2.90000, 'nieve':0.0, 'precp_h':4.0, 'viento': 9.6598}

    # Convertir 'valores_caracteristicas' en un DataFrame
    datos_prueba = pd.DataFrame([valores_caracteristicas])

    # Hacer una predicción con el modelo
    prediccion_2 = rr.predict(datos_prueba)

    # Imprimir la predicción
    print("Predicción:", prediccion_2)

    def obtener_valores_caracteristicas():
        valores = {}
        print("Ingrese los valores de las características:")
        valores["temp_max"] = float(input("Temperatura máxima: "))
        valores["temp_min"] = float(input("Temperatura mínima: "))
        valores["temp_prom"] = (valores["temp_max"] + valores["temp_min"]) / 2
        valores["precp"] = float(input("Precipitación: "))
        valores["lluvia"] = float(input("Lluvia: "))
        valores["nieve"] = float(input("Nieve: "))
        valores["precp_h"] = float(input("Precipitación (horas): "))
        valores["viento"] = float(input("Viento: "))
        return valores

    def hacer_prediccion(modelo, valores):
        datos_prueba = pd.DataFrame([valores])
        prediccion_5 = modelo.predict(datos_prueba)
        return prediccion_5

    # Llamar a la función para obtener los valores de las características
    valores = obtener_valores_caracteristicas()

    # Hacer predicción con los valores ingresados por el usuario
    prediccion_5 = hacer_prediccion( rr, valores)
    # Mostrar la predicción al usuario
    print("La predicción es:", prediccion_5)
        
#uno()
#dos()
#tres() #FUNCION Dataset para predicciones GRAFICA TEM MIN AND MAX
# cuatro()
calculadora()
 # 




