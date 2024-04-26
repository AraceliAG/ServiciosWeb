// Reemplaza 'TU_API_KEY' con tu propia API Key de OpenWeatherMap
// const apiKey = '0de3e31e737062e03a2a9553c4b4fb11';
// const latitud = '20.6167';
// const longitud = '-103.2333';

// URL de la API de OpenWeatherMap para obtener el clima actual por coordenadas
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather?lat=20.6167&lon=-103.2333&appid=0de3e31e737062e03a2a9553c4b4fb11&units=metric';


// Realiza una solicitud GET a la API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Procesa los datos recibidos
    const temperatura = data.main.temp;
    const descripcion = data.weather[0].description;
    
    // Actualiza el contenido del elemento HTML con los datos del clima
    const climaElement = document.getElementById('climaTonala');
    climaElement.innerHTML = `El clima actual de tonala ${descripcion} con una temperatura de ${temperatura}°C.`;

  })
  .catch(error => {
    console.error('Error al obtener datos del clima:', error);
  });
