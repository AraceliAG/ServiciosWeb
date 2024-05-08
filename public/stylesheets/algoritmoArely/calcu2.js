// Importar TensorFlow.js

// Manejar el envío del formulario

// Definir la función de entrenamiento del modelo de regresión lineal
async function entrenarModelo(df_historica) {
    // Convertir los datos de entrada y salida en tensores
    const xs = tf.tensor2d(df_historica.map(data => [data.temp_max, data.temp_min, data.temp_prom, data.precp, data.precp_h, data.viento]));
    const ys = tf.tensor2d(df_historica.map(data => [data.target]));

    // Definir el modelo de regresión lineal
    const modelo = tf.sequential();
    modelo.add(tf.layers.dense({units: 1, inputShape: [6]}));

    // Compilar el modelo
    modelo.compile({loss: 'meanSquaredError', optimizer: 'sgd'});

    // Entrenar el modelo
    await modelo.fit(xs, ys, {epochs: 100});

    return modelo;
}

// Definir la función para hacer una predicción del clima máximo
function predecirClimaMaximo(modelo, valores) {
    // Convertir los valores del formulario en un tensor
    const entrada = tf.tensor2d([[valores.temp_max, valores.temp_min, valores.temp_prom, valores.precp, valores.precp_h, valores.viento]]);
    
    // Hacer la predicción
    const prediccion = modelo.predict(entrada);

    // Obtener el valor de la predicción
    const prediccionValor = prediccion.dataSync()[0];

    return prediccionValor;
}

// Evento de envío del formulario
document.getElementById("formulario").addEventListener("submit", async function(event) {
    event.preventDefault(); // Evitar que el formulario se envíe de forma tradicional

    // Obtener los valores del formulario
    let valores = {
        "temp_max": parseFloat(document.getElementById("temp_max").value),
        "temp_min": parseFloat(document.getElementById("temp_min").value),
        "temp_prom": (parseFloat(document.getElementById("temp_max").value) + parseFloat(document.getElementById("temp_min").value)) / 2,
        "precp": parseFloat(document.getElementById("precp").value),
        "lluvia": parseFloat(document.getElementById("precp").value), // Corregido
        "nieve": 0, 
        "precp_h": parseFloat(document.getElementById("precp_h").value),
        "viento": parseFloat(document.getElementById("viento").value)
    };
    
    var df_historica = [
        {"fecha": "2000-01-01", "temp_max": 24.9135, "temp_min": 11.9135, "temp_prom": 18.123919, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 8.78872}, 
        {"fecha": "2000-01-02", "temp_max": 24.563501, "temp_min": 12.6635, "temp_prom": 18.005167, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 9.255571}, 
        {"fecha": "2000-01-03", "temp_max": 24.963501, "temp_min": 13.1135, "temp_prom": 18.094751, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 8.825508}, 
        {"fecha": "2000-01-04", "temp_max": 24.3635, "temp_min": 9.763499, "temp_prom": 17.95725, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 9.422101}, 
        {"fecha": "2000-01-05", "temp_max": 23.2635, "temp_min": 8.7135, "temp_prom": 16.242666, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 8.217153}, 
        {"fecha": "2000-01-06", "temp_max": 23.5135, "temp_min": 12.6135, "temp_prom": 17.373915, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 10.182337}, 
        {"fecha": "2000-01-07", "temp_max": 23.1635, "temp_min": 11.1135, "temp_prom": 16.992668, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 10.1376915}, 
        {"fecha": "2000-01-08", "temp_max": 23.6135, "temp_min": 12.4135, "temp_prom": 17.623919, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 7.5685663}, 
        {"fecha": "2000-01-09", "temp_max": 23.3635, "temp_min": 12.513499, "temp_prom": 17.217665, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 9.746631}, 
        {"fecha": "2000-01-10", "temp_max": 24.2635, "temp_min": 9.7135, "temp_prom": 17.430166, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 7.289444}, 
        {"fecha": "2000-01-11", "temp_max": 25.1135, "temp_min": 10.763499, "temp_prom": 18.234335, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 6.2145634}, 
        {"fecha": "2000-01-12", "temp_max": 25.9135, "temp_min": 11.4635, "temp_prom": 18.601002, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 8.12197}, 
        {"fecha": "2000-01-13", "temp_max": 26.6635, "temp_min": 9.763499, "temp_prom": 18.744751, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 12.144331}, 
        {"fecha": "2000-01-14", "temp_max": 24.4135, "temp_min": 11.1635, "temp_prom": 16.765583, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 19.296133}, 
        {"fecha": "2000-01-15", "temp_max": 22.313501, "temp_min": 9.8635, "temp_prom": 15.388499, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 16.62249}, 
        {"fecha": "2000-01-16", "temp_max": 22.6135, "temp_min": 8.813499, "temp_prom": 15.661415, "precp": 0.0, "lluvia": 0.0, "nieve": 0.0, "precp_h": 0.0, "viento": 11.720751}
    ];

    

   

    // Entrenar el modelo
    const modelo = await entrenarModelo(df_historica);

    // Hacer la predicción del clima máximo
    const prediccion = predecirClimaMaximo(modelo, valores);

    // Mostrar la predicción en la página
    document.getElementById("resultado").innerText = "La predicción del clima máximo es: " + prediccion;
});