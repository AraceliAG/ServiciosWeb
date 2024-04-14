
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

