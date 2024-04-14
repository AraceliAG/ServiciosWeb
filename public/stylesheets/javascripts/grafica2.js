// Reemplaza la definición de la variable 'chart_data' con los datos generados en Python
var chart_data = [
    // Aquí se colocarán los datos generados en Python
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

// Establece los datos generados en Python en el gráfico
areaSeries.setData(chart_data);


