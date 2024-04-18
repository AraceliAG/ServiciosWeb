var chartData = [{"time": "Semestre 1", "value": 49.833333333333336}, {"time": "Semestre 2", "value": 77.70175438596492}, {"time": "Semestre 3", "value": 64.85}, {"time": "Semestre 4", "value": 78.96428571428571}, {"time": "Semestre 5", "value": 59.164556962025316}, {"time": "Semestre 6", "value": 77.08666666666667}, {"time": "Semestre 7", "value": 55.26829268292683}, {"time": "Semestre 8", "value": 79.39516129032258}, {"time": "Semestre 9", "value": 55.875}];

var ctx = document.getElementById('myChart2').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chartData.map(data => data.time),
        datasets: [{
            label: 'HUMEDAD',
            data: chartData.map(data => data.value),
            backgroundColor: 'rgb(30,144,255)',
            borderColor: 'rgb(30,144,255)',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        width: '100%', // Ocupar todo el ancho del contenedor
        height: '100%' // Ocupar todo el alto del contenedor
    }
});
