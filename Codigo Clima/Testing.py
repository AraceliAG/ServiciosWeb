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
db = client["Clima_Test"]

# Selecciona la colección en la que deseas guardar los datos
collection = db["Datos"]

start_urls = ['https://www.wunderground.com/weather/mx/guadalajara/KJAGUADA1',
              'https://www.wunderground.com/weather/mx/zapopan/IZAPOP11',
              'https://www.wunderground.com/weather/mx/tlaquepaque/ITLAQU4',
              'https://www.wunderground.com/weather/mx/tonalá',
              'https://www.wunderground.com/weather/mx/tlajomulco-de-zúñiga/ITLAJO3'
              ]

second_urls = ['https://www.wunderground.com/health/mx/guadalajara/KJAGUADA1?cm_ven=localwx_modaq',
               'https://www.wunderground.com/health/mx/zapopan/IZAPOP11?cm_ven=localwx_modaq',
               'https://www.wunderground.com/health/mx/tlaquepaque/ITLAQU4?cm_ven=localwx_modaq',
               'https://www.wunderground.com/health/mx/tonalá?cm_ven=localwx_modaq',
               'https://www.wunderground.com/health/mx/tlajomulco-de-zúñiga/ITLAJO3?cm_ven=localwx_modaq']

third_url = ['https://www.wunderground.com/precipitation/mx/guadalajara/KJAGUADA1?cm_ven=localwx_modprecip',
             'https://www.wunderground.com/precipitation/mx/zapopan/IZAPOP11?cm_ven=localwx_modprecip',
             'https://www.wunderground.com/precipitation/mx/tlaquepaque/ITLAQU4?cm_ven=localwx_modprecip',
             'https://www.wunderground.com/precipitation/mx/tonalá?cm_ven=localwx_modprecip',
             'https://www.wunderground.com/precipitation/mx/tlajomulco-de-zúñiga/ITLAJO3?cm_ven=localwx_modprecip']


def insertarDatos (ciudad, current, real_feal, air_quality, pollen, uv_index, precipitation, current_datetime):
    collection.insert_one({
                    "ciudad": ciudad,
                    "current": current,
                    "real_feal": real_feal,
                    "air_quality": air_quality,
                    "pollen": pollen,
                    "uv_index": uv_index,
                    "precipitation": precipitation,
                    "timestamp": current_datetime
                })

def extraer_clima():

    driver = webdriver.Edge()
    
    for i, url in enumerate (start_urls):
        driver.get(url)
        time.sleep(2)
    
        ciudad = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[2]/lib-city-header/div[1]/div/h1/span[1]').text
        current = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[2]/lib-display-unit/span').text
        real_feal = driver.find_element(By.XPATH, '//*[@id="inner-content"]/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[3]/span').text
        ciudad= ciudad.replace(', Mexico Weather Conditions', '')
        
        second_url = second_urls[i]
        driver.get(second_url)
        time.sleep(2)
        air_quality = driver.find_element(By.XPATH, '//*[@id="airqualityindex_section"]/div/div/div/div[2]/div[2]/div[1]/div[2]').text
        pollen = driver.find_element(By.XPATH, '//*[@id="pollen_section"]/div/div[2]').text
        uv_index = driver.find_element(By.XPATH, '//*[@id="uv_section"]/div/div[3]/div[2]').text
        
        third_urlv = third_url[i]
        driver.get(third_urlv)
        time.sleep(2)
        precipitation = driver.find_element(By.XPATH, '//*[@id="precip-graph"]/div/lib-precipitation-graph-alert/div/h2/span').text
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        insertarDatos(ciudad, current, real_feal, air_quality, pollen, uv_index, precipitation, current_datetime)
        
    driver.close()

schedule.every(3).minutes.do(extraer_clima)
extraer_clima()

while True:
    schedule.run_pending()
    time.sleep(1)