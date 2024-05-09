import asyncio
import websockets
import pandas as pd
from sklearn.linear_model import Ridge
import json

PORT = 6969
clientes = set()

async def websocket_handler(websocket, path):
    clientes.add(websocket)
    try:
        while True:
            try:
                message = await websocket.recv()
                if message == "exit":
                    break
                else:
                    # Convertir el mensaje JSON a un diccionario de Python
                    datos = json.loads(message)
                    
                    # Realizar la predicción
                    prediccion = hacer_prediccion(rr, datos, df_historica, predictors)
                    
                    # Enviar la predicción de vuelta a todos los clientes conectados
                    await asyncio.gather(*[cliente.send(json.dumps( prediccion)) for cliente in clientes])
            except websockets.ConnectionClosed:
                break
    finally:
        clientes.remove(websocket)

async def start_websocket_server():
    async with websockets.serve(websocket_handler, "localhost", PORT):
        print(f"Servidor WebSocket iniciado correctamente.")
        await asyncio.Future()

def run_server():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_websocket_server())

if __name__ == "__main__":
    # Lectura de datos
    df_2000_2010 = pd.read_csv('2000 - 2010 - APIH.csv')
    df_2010_2022 = pd.read_csv('2010 - 2022 - APIH.csv')

    # Concatenar los DataFrames
    dfs = [df_2000_2010, df_2010_2022]
    df_historica = pd.concat(dfs, ignore_index=True)
    df_historica = df_historica.drop(columns=['Unnamed: 0'])  # Eliminar columnas que no sirven

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
    df_historica = df_historica.ffill()  # Solucionar el target de la última fecha

    rr = Ridge(alpha=.1)
    predictors = df_historica.columns[~df_historica.columns.isin(["target"])]

    def hacer_prediccion(modelo, valores, df_historica, predictors):
        # Calcular temp_prom a partir de temp_max y temp_min
        valores["temp_prom"] = (valores["temp_max"] + valores["temp_min"]) / 2
        
        # Proporcionar valores predeterminados para lluvia y nieve
        valores["lluvia"] = 0.0
        valores["nieve"] = 0.0
        
        # Convertir los valores del diccionario en un DataFrame
        datos_prueba = pd.DataFrame([valores])
        
        # Seleccionar solo las características necesarias para la predicción
        datos_prueba = datos_prueba[predictors]
        
        # Ajustar el modelo a los datos de entrenamiento
        modelo.fit(df_historica[predictors], df_historica["target"])
    
    # Realizar la predicción
        return float(modelo.predict(datos_prueba))

    def obtener_valores_caracteristicas():
        valores = {}
        print("Ingrese los valores de las características:")
        valores["temp_max"] = float(input("Temperatura máxima: "))
        valores["temp_min"] = float(input("Temperatura mínima: "))
        valores["precp"] = float(input("Precipitación: "))
        valores["precp_h"] = float(input("Precipitación (horas): "))
        valores["viento"] = float(input("Viento: "))
        return valores

    def run_server():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(start_websocket_server())

    run_server()
