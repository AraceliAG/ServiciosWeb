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

def calculadora():
    #daily_dataframe.to_csv('2010 - 2022 - APIH.csv', index=True) # Para guardar sin el índice del DataFrame
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

    df_historica['fecha'] = df_historica['fecha'].dt.date
  
    df_historica['fecha'] = pd.to_datetime(df_historica['fecha'])
 
    nulos_totales = df_historica.isnull().sum()
   
    registros_por_año = df_historica.groupby(df_historica['fecha'].dt.year).size()
 
    df_historica = df_historica.set_index('fecha')

    
    df_historica["target"] = df_historica.shift(-1)["temp_max"]
    df_historica = df_historica.ffill() # Solucionar el target de la ultima fecha

    
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

    datos_prueba = pd.DataFrame([valores_caracteristicas])

    prediccion_2 = rr.predict(datos_prueba)


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

    valores = obtener_valores_caracteristicas()

    prediccion_5 = hacer_prediccion( rr, valores)

    print("La predicción es:", prediccion_5)

calculadora()

        




