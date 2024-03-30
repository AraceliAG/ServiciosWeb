import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import pymongo

# Conéctate a tu clúster de MongoDB
client = pymongo.MongoClient("mongodb+srv://POE:Manu7190@cluster0.avhhgxe.mongodb.net/?retryWrites=true&w=majority")
#mongodb+srv://Ara:<cEGeCjYRsWoluKg5>@clustertest.p1rrutb.mongodb.net/

# Selecciona la base de datos que deseas utilizar
db = client["Historico"]

# Selecciona la colección en la que deseas guardar los datos
collection = db["Datos"]

def generar_urls_desde_2018():
    meses = {
        "January": "enero",
        "February": "febrero",
        "March": "marzo",
        "April": "abril",
        "May": "mayo",
        "June": "junio",
        "July": "julio",
        "August": "agosto",
        "September": "septiembre",
        "October": "octubre",
        "November": "noviembre",
        "December": "diciembre"
    }
    
    urls = []
    fecha_actual = datetime.date.today()
    fecha_inicial = datetime.date(2020, 11, 15)
    
    while fecha_inicial <= fecha_actual:
        mes_esp = meses[fecha_inicial.strftime("%B")]
        url = f"https://www.tutiempo.net/registros/mmgl/{fecha_inicial.day}-{mes_esp}-{fecha_inicial.year}.html"
        urls.append(url)
        fecha_inicial += datetime.timedelta(days=1)
    
    return urls

def insertarDatos(fecha, nubosidad, temperatura, viento, humedad, presion):
    collection.insert_one({
                    "nubosidad": nubosidad,
                    "fecha": fecha,
                    "temperatura": temperatura,
                    "viento": viento,
                    "humedad": humedad,
                    "presion": presion
                    
                })

def extraer_clima():
    driver = webdriver.Edge()
    
    for url in generar_urls_desde_2018():
        driver.get(url)
        time.sleep(2)
    
        fecha = driver.find_element(By.XPATH, '//*[@id="HistoricosData"]/div/table/tbody/tr[1]/th').text
        nubosidad = driver.find_element(By.XPATH, '//*[@id="HistoricosData"]/div/table/tbody/tr[3]/td[2]/span').text 
        temperatura = driver.find_element(By.XPATH,'//*[@id="HistoricosData"]/div/table/tbody/tr[3]/td[3]').text
        viento = driver.find_element(By.XPATH,'//*[@id="HistoricosData"]/div/table/tbody/tr[3]/td[4]').text
        humedad = driver.find_element(By.XPATH,'//*[@id="HistoricosData"]/div/table/tbody/tr[3]/td[5]').text
        presion = driver.find_element(By.XPATH,'//*[@id="HistoricosData"]/div/table/tbody/tr[3]/td[6]').text
        
        

        insertarDatos(fecha, nubosidad, temperatura, viento, humedad, presion)
    
    driver.close()

#schedule.every(3).minutes.do(extraer_clima)

extraer_clima()

while True:
    schedule.run_pending()
    time.sleep(1)
