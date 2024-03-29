import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import pymongo
from datetime import datetime, timedelta
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException

# Conéctate a tu clúster de MongoDB
client = pymongo.MongoClient("mongodb+srv://POE:Manu7190@cluster0.avhhgxe.mongodb.net/?retryWrites=true&w=majority")
#mongodb+srv://Ara:<cEGeCjYRsWoluKg5>@clustertest.p1rrutb.mongodb.net/

# Selecciona la base de datos que deseas utilizar
db = client["Historico"]

# Selecciona la colección en la que deseas guardar los datos
collection = db["Datos"]

urls = ['https://www.tutiempo.net/registros/mmgl/1-enero-2018.html']

#diccionario de datos dado a que la funcion que convierte los numeros de meses a su nombre lo hace in ingles
meses_espanol = {
    'January': 'enero',
    'February': 'febrero',
    'March': 'marzo',
    'April': 'abril',
    'May': 'mayo',
    'June': 'junio',
    'July': 'julio',
    'August': 'agosto',
    'September': 'septiembre',
    'October': 'octubre',
    'November': 'noviembre',
    'December': 'diciembre'
}

fecha_inicio = datetime(2018, 1, 1)
fecha_fin = datetime(2022, 12, 31)

urls = []

# Iterar sobre cada día en el rango de fechas y generar la URL correspondiente
fecha_actual = fecha_inicio
while fecha_actual <= fecha_fin:

    nombre_mes_ingles = fecha_actual.strftime('%B')
    nombre_mes_espanol = meses_espanol[nombre_mes_ingles]
    url = f'https://www.tutiempo.net/registros/mmgl/{fecha_actual.day}-{nombre_mes_espanol}-{fecha_actual.year}.html'
    urls.append(url)
    
    # Avanzamos al siguiente día en teoria
    fecha_actual += timedelta(days=1)

def insertarDatos (clima):
    collection.insert_one({
                    "clima": clima,
                })

def extraer_clima():
    driver = webdriver.Edge()
    
    for url in urls:
        try:
            driver.get(url)
            time.sleep(2)
            
            clima = driver.find_element(By.XPATH, '//*[@id="HistoricosData"]/div/table/tbody/tr[7]/td[2]/span').text
            insertarDatos(clima)
        
        # Captura la excepción si no se encuentra el elemento
        except NoSuchElementException:
            print(f"No se encontraron datos climáticos para la URL: {url}. Saltando al siguiente día.")
        
        # Captura la excepción si la página no existe o no está disponible
        except (TimeoutException, WebDriverException):
            print(f"La página {url} no existe o no está disponible. Saltando al siguiente día.")
        
        finally:
            driver.quit()

#schedule.every(7).seconds.do(extraer_clima)

extraer_clima()

while True:
    schedule.run_pending()
    time.sleep(1)
