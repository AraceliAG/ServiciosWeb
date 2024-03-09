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
db = client["Medicamentos"]

# Selecciona la colección en la que deseas guardar los datos
collection = db["Datos"]

farmacias_guadalajara = ['']
farmacias_del_ahorro = ['']
walmart = ['']
soriana = ['']



def extraer():
    driver = webdriver.Edge()

    for url in start_urls:
        driver.get(url)
        time.sleep(2)

        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
        availability = driver.find_element(By.XPATH, '').text
        
    
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Inserta los datos en MongoDB
        collection.insert_one({
                    "Nombre": name,
                    "Precio": price,
                    "Disponibilidad": availability,
                    "timestamp": current_datetime
                })
       
    driver.close()
    


schedule.every(3).minutes.do(extraer)


extraer()


while True:
    schedule.run_pending()
    time.sleep(1)
