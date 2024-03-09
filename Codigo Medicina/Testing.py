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

farmacias_guadalajara = ['https://www.farmaciasguadalajara.com/aspirina-500-mg-40-tabletas-35645#']
farmacias_del_ahorro = ['https://www.fahorro.com/aspirina-analgesico-40-tabletas.html']
walmart = ['https://super.walmart.com.mx/ip/aspirina-40-tabletas-500-mg/00750100849196?from=/search']
soriana = ['https://www.soriana.com/analgesico-aspirina-para-dolor-de-cabeza-dolor-corporal-y-fiebre-40-tabletas-nbsp/361111.html']



def aspirina():
    driver = webdriver.Edge()

    for url in farmacias_guadalajara:
        driver.get(url)
        time.sleep(2)

        farmacia = "Farmacias Guadalajara"
        name = driver.find_element(By.XPATH, '//*[@id="fgProductName"]').text
        price = driver.find_element(By.XPATH, '//*[@id="offerPrice_3074457345616708123"]').text
       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
                # Inserta los datos en MongoDB
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
         
    """  for url in farmacias_del_ahorro:
        driver.get(url)
        time.sleep(2)

        farmacia = "Farmacias del Ahorro"
        name = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[2]/div/div[1]/div[1]/h1/span').text
        price = driver.find_element(By.XPATH, '//*[@id="product-price-48539"]/span').text
       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                  
                  # Inserta los datos en MongoDB
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                }) 
    """   
        
    for url in walmart:
        driver.get(url)
        time.sleep(2)

        farmacia = "Walmart"
        name = driver.find_element(By.XPATH, '//*[@id="main-title"]').text
        price = driver.find_element(By.XPATH, '//*[@id="maincontent"]/section/main/div[2]/div[2]/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span/span[2]/span').text
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })       
    
    for url in soriana:
        driver.get(url)
        time.sleep(2)
        
        farmacia = "Soriana"
        name = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div/div[1]/h1').text
        price = driver.find_element(By.XPATH, '//*[@id="maincontent"]/div[3]/div/div/div[3]/div[3]/div[1]/div/div/div[1]/div[1]/span/span').text
       
                   
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
       
    driver.close()
    

def suero():
    driver = webdriver.Edge()

    for url in farmacias_guadalajara:
        driver.get(url)
        time.sleep(2)

        farmacia = "Farmacias Guadalajara"
        name = driver.find_element(By.XPATH, '//*[@id="fgProductName"]').text
        price = driver.find_element(By.XPATH, '//*[@id="offerPrice_3074457345616708123"]').text
       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
           
        
    for url in walmart:
        driver.get(url)
        time.sleep(2)

        farmacia = "Walmart"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })       
    
    for url in soriana:
        driver.get(url)
        time.sleep(2)
        
        farmacia = "Soriana"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
       
                   
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
       
    driver.close()

def omeprazol():
    driver = webdriver.Edge()

    for url in farmacias_guadalajara:
        driver.get(url)
        time.sleep(2)

        farmacia = "Farmacias Guadalajara"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
         
   
    for url in walmart:
        driver.get(url)
        time.sleep(2)

        farmacia = "Walmart"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })       
    
    for url in soriana:
        driver.get(url)
        time.sleep(2)
        
        farmacia = "Soriana"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
       
                   
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
       
    driver.close()

def paracetamol():
    driver = webdriver.Edge()

    for url in farmacias_guadalajara:
        driver.get(url)
        time.sleep(2)

        farmacia = "Farmacias Guadalajara"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
           
        
    for url in walmart:
        driver.get(url)
        time.sleep(2)

        farmacia = "Walmart"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })       
    
    for url in soriana:
        driver.get(url)
        time.sleep(2)
        
        farmacia = "Soriana"
        name = driver.find_element(By.XPATH, '').text
        price = driver.find_element(By.XPATH, '').text
                       
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
        
        collection.insert_one({
                    "Establecimiento": farmacia,
                    "Nombre": name,
                    "Precio": price,
                    "timestamp": current_datetime
                })
       
    driver.close()

schedule.every(1).minutes.do(aspirina)
schedule.every(1).minutes.do(suero)
schedule.every(1).minutes.do(omeprazol)
schedule.every(1).minutes.do(paracetamol)


aspirina()
suero()
omeprazol()
paracetamol()

while True:
    schedule.run_pending()
    time.sleep(1)
