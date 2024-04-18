var chartData = [{"time": "Semestre 1", "value": 11.944444444444445}, {"time": "Semestre 2", "value": 17.017543859649123}, {"time": "Semestre 3", "value": 11.983333333333333}, {"time": "Semestre 4", "value": 18.285714285714285}, {"time": "Semestre 5", "value": 14.20253164556962}, {"time": "Semestre 6", "value": 18.273333333333333}, {"time": "Semestre 7", "value": 12.609756097560975}, {"time": "Semestre 8", "value": 17.951612903225808}, {"time": "Semestre 9", "value": 13.1875}];



var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: chartData.map(data => data.time),
        datasets: [{
            label: 'TEMPERATURA',
            data: chartData.map(data => data.value),
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
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

