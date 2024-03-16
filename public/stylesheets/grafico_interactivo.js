const fs = require('fs');

// Leer los datos del archivo JSON generado por Node.js
const data = JSON.parse(fs.readFileSync('grafico_interactivo.json', 'utf8'));

// Crear el gráfico utilizando los datos cargados
const layout = {
    title: 'Gráfico interactivo de temperatura real',
    xaxis: { title: 'Timestamp' },
    yaxis: { title: 'Temperatura Real (°C)' }
};

Plotly.newPlot('grafico', data.data, layout);
