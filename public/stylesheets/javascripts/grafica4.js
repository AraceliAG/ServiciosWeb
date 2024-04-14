var charData = [{"time": "2018-01-01", "value": 11}, {"time": "2018-01-02", "value": 10}, {"time": "2018-01-03", "value": 10}, {"time": "2018-01-04", "value": 9}, {"time": "2018-01-05", "value": 11}, {"time": "2018-01-06", "value": 8}, {"time": "2018-01-07", "value": 8}, {"time": "2018-01-08", "value": 7}, {"time": "2018-01-09", "value": 6}, {"time": "2018-01-10", "value": 8}, {"time": "2018-01-11", "value": 12}, {"time": "2018-01-12", "value": 4}, {"time": "2018-01-13", "value": 3}, {"time": "2018-01-14", "value": 6}, {"time": "2018-01-15", "value": 3}, {"time": "2018-01-16", "value": 4}, {"time": "2018-01-17", "value": 14}];

// Configurar la gráfica
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chartData.map(data => data.time), // Suponiendo que 'time' es la etiqueta de tu eje X
        datasets: [{
            label: 'Valor',
            data: chartData.map(data => data.value), // Suponiendo que 'value' es tu dato en el eje Y
            backgroundColor: 'rgba(255, 99, 132, 0.2)', // Color de fondo del gráfico
            borderColor: 'rgba(255, 99, 132, 1)', // Color de la línea del gráfico
            borderWidth: 1 // Ancho de la línea del gráfico
        }]
    },
    options: {
        // Opciones de configuración adicionales (puedes personalizar según tus necesidades)
    }
});