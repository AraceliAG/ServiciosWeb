
var data = [
    { time: '2024-01-01', value: 20 },
    { time: '2024-01-02', value: 22 },
    { time: '2024-01-03', value: 19 },
    // Añade más datos aquí...
];

var chart = LightweightCharts.createChart(document.body, {
    width: 1000,
    height: 500,
    layout: {
        textColor: '#d1d4dc',
        background: {
            type: 'solid',
            color: '#000000',
        },
    },
    rightPriceScale: {
        scaleMargins: {
            top: 0.3,
            bottom: 0.25,
        },
    },
    crosshair: {
        vertLine: {
            width: 5,
            color: 'rgba(224, 227, 235, 0.1)',
            style: 0,
        },
        horzLine: {
            visible: false,
            labelVisible: false,
        },
    },
    grid: {
        vertLines: {
            color: 'rgba(42, 46, 57, 0)',
        },
        horzLines: {
            color: 'rgba(42, 46, 57, 0)',
        },
    },
});

var areaSeries = chart.addAreaSeries({
    topColor: 'rgba(38, 198, 218, 0.56)',
    bottomColor: 'rgba(38, 198, 218, 0.04)',
    lineColor: 'rgba(38, 198, 218, 1)',
    lineWidth: 2,
    crossHairMarkerVisible: false,
});

// Establece los datos de temperatura en el gráfico
areaSeries.setData(data);

// Añade la leyenda para mostrar la temperatura actual en el cursor
document.body.style.position = 'relative';

var legend = document.createElement('div');
legend.classList.add('legend');
document.body.appendChild(legend);

var firstRow = document.createElement('div');
firstRow.innerText = 'Temperatura (°C)';
firstRow.style.color = 'white';
legend.appendChild(firstRow);

chart.subscribeCrosshairMove((param) => {
    if (param.time) {
        const dataPoint = areaSeries.priceLineAtIndex(param.time);
        if (dataPoint) {
            firstRow.innerText = 'Temperatura (°C): ' + dataPoint.price.toFixed(2);
        }
    } else {
        firstRow.innerText = 'Temperatura (°C)';
    }
});
