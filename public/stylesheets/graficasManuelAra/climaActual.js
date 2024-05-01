

// URL API
const apiUrl = 'https://api.openweathermap.org/data/2.5/weather?lat=20.6167&lon=-103.2333&appid=0de3e31e737062e03a2a9553c4b4fb11&units=metric';


fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // PROCESA DATOS
    const temperatura = data.main.temp;
    const descripcion = data.weather[0].description;
    const humedad = data.main.humidity; // Obtener humedad
    const velocidadViento = data.wind.speed; // Obtener velocidad del viento

    // MAPEA Y TRADUCE
    const descripcionEspañol = obtenerDescripcionEnEspañol(descripcion);

    // MANDA TEMPERATURA 
    const temperaturaElement = document.querySelector('.temperaturaT');
    temperaturaElement.innerHTML = `${temperatura} <span>°C</span>`;

    // MANDA DESCRIPCIÓN
    const descripcionElement = document.querySelector('.description');
    descripcionElement.textContent = descripcionEspañol;

    // MANDA HUMEDAD
    const humedadElement = document.querySelector('.humedad .info-humidity span');
    humedadElement.textContent = `${humedad}%`;

    // MANDA VELOCIDAD DEL VIENTO
    const velocidadVientoElement = document.querySelector('.wind .info-humidity span');
    velocidadVientoElement.textContent = `${velocidadViento} Km/h`;
  })
  .catch(error => {
    console.error('Error al obtener datos del clima:', error);
  });


// FUNCION PARA OBTENER TRADUCCION
function obtenerDescripcionEnEspañol(descripcion) {
  const descripcionesEnIngles = {
    'clear sky': 'cielo despejado',
    'few clouds': 'pocas nubes',
    'scattered clouds': 'nubes dispersas',
    'broken clouds': 'nubes dispersas',
    'shower rain': 'lluvia ligera',
    'rain': 'lluvia',
    'thunderstorm': 'tormenta eléctrica',
    'snow': 'nieve',
    'mist': 'niebla',
    'overcast clouds': 'Nublado'
  };

  //SI NO EXISTE TRADUCCION SE MANDA ORIGINA
  return descripcionesEnIngles.hasOwnProperty(descripcion) ? descripcionesEnIngles[descripcion] : descripcion;
}


