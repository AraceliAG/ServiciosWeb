       
var chart_data = [{"time": "2018-01-01", "value": 11}, {"time": "2018-01-02", "value": 10}, 
{"time": "2018-01-03", "value": 10}, {"time": "2018-01-04", "value": 9}, 
{"time": "2018-01-05", "value": 11}, {"time": "2018-01-06", "value": 8}, 
{"time": "2018-01-07", "value": 8}, {"time": "2018-01-08", "value": 7}, 
{"time": "2018-01-09", "value": 6}, {"time": "2018-01-10", "value": 8},
{"time": "2018-01-11", "value": 12}, {"time": "2018-01-12", "value": 4},
 {"time": "2018-01-13", "value": 3}, {"time": "2018-01-14", "value": 6},
  {"time": "2018-01-15", "value": 3}, {"time": "2018-01-16", "value": 4},
   {"time": "2018-01-17", "value": 14}, {"time": "2018-01-18", "value": 8},
    {"time": "2018-01-19", "value": 12}, {"time": "2018-01-20", "value": 9},
     {"time": "2018-01-21", "value": 10}, {"time": "2018-01-22", "value": 7},
      {"time": "2018-01-23", "value": 19}, {"time": "2018-01-24", "value": 11},
       {"time": "2018-01-25", "value": 13}, {"time": "2018-01-26", "value": 11},
        {"time": "2018-01-27", "value": 12}, {"time": "2018-01-28", "value": 9}, 
        {"time": "2018-01-29", "value": 12}, {"time": "2018-01-30", "value": 10},
         {"time": "2018-01-31", "value": 11}, {"time": "2018-02-01", "value": 9}, 
         {"time": "2018-02-02", "value": 17}, {"time": "2018-02-03", "value": 13},
          {"time": "2018-02-04", "value": 13}, {"time": "2018-02-05", "value": 13}, 
          {"time": "2018-02-06", "value": 8}, {"time": "2018-02-07", "value": 12}, {"time": "2018-02-08", "value": 17}, {"time": "2018-02-09", "value": 14}, {"time": "2018-02-10", "value": 12}, {"time": "2018-02-11", "value": 11}, {"time": "2018-02-12", "value": 9}, {"time": "2018-02-13", "value": 12}, {"time": "2018-02-14", "value": 19}, {"time": "2018-02-15", "value": 16}, {"time": "2018-02-16", "value": 16}, {"time": "2018-02-17", "value": 16}, {"time": "2018-02-18", "value": 16}, {"time": "2018-02-19", "value": 17}, {"time": "2018-02-20", "value": 8}, {"time": "2018-02-21", "value": 11}, {"time": "2018-02-22", "value": 9}, {"time": "2018-02-23", "value": 13}, {"time": "2018-02-24", "value": 20}, {"time": "2018-02-25", "value": 11}, {"time": "2018-02-26", "value": 9}, {"time": "2018-02-27", "value": 13}, {"time": "2018-02-28", "value": 23}, {"time": "2018-03-01", "value": 12}, {"time": "2018-03-02", "value": 17}, {"time": "2018-03-03", "value": 13}];

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






function convertirFormato(datos) {
    // Creamos una nueva lista para almacenar los datos convertidos
    var datosConvertidos = [];

    // Iteramos sobre cada objeto en la lista de datos
    datos.forEach(function(item) {
        // Extraemos las claves y valores del objeto actual
        var time = item["time"];
        var value = item["value"];

        // Creamos un nuevo objeto con el formato deseado y lo añadimos a la lista de datos convertidos
        datosConvertidos.push({ time: time, value: value });
    });

    // Retornamos la lista de datos convertidos
    return datosConvertidos;
}

// Ejemplo de uso:
var datosOriginales = [{"time": "2021-12-31", "value": 10}];
var datosConvertidos = convertirFormato(datosOriginales);

