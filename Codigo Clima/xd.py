import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime

start_urls = ['https://www.wunderground.com/weather/mx/guadalajara/KJAGUADA1']
second_urls = ['https://www.wunderground.com/health/mx/guadalajara/KJAGUADA1?cm_ven=localwx_modaq']
third_url = ['https://www.wunderground.com/precipitation/mx/guadalajara/KJAGUADA1?cm_ven=localwx_modprecip']

xd = ['https://es.weatherspark.com/h/d/3836/2021/1/24/Tiempo-hist%C3%B3rico-el-domingo-24-de-enero-de-2021-en-Tonal%C3%A1-M%C3%A9xico']


def extraer_Temperatura ():
    
    
     driver = webdriver.Edge()

     for url in xd:
        driver.get(url)
        time.sleep(2)
        mes =  driver.find_element(By.XPATH, '//*[@id="Report-Content"]/div[2]/div/div/div/div[2]/svg/g[33]/g/text[1]').text
        print(mes)
        with open("datos-clima-test.csv", "a") as f:
                f.write(f"{mes}\n")
        driver.close()
    
    
schedule.every(2).minutes.do(extraer_Temperatura)


# extraer_clima()
extraer_Temperatura()


while True:
    schedule.run_pending()
    time.sleep(1)
