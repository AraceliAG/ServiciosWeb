// Reemplaza 'TU_API_KEY' con tu propia API Key de OpenWeatherMap
const apiKey = 'TU_API_KEY';
const ciudad = 'Tonalá';
const estado = 'Jalisco';

// URL de la API de OpenWeatherMap para obtener el clima actual por ciudad
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${ciudad},${estado}&appid=${apiKey}&units=metric`;

// Realiza una solicitud GET a la API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Procesa los datos recibidos
    const temperatura = data.main.temp;
    const descripcion = data.weather[0].description;
    
    // Actualiza el contenido del elemento HTML con los datos del clima
    const climaElement = document.getElementById('climaTonala');
    climaElement.innerHTML = `El clima actual en Tonalá, Jalisco es ${descripcion} con una temperatura de ${temperatura}°C.`;
  })
  .catch(error => {
    console.error('Error al obtener datos del clima:', error);
  });
