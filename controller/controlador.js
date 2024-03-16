const cargarDatos = require('../model/modelo')
const plotly = require('plotly')('username', 'apiKey');
const fs = require('fs');


module.exports = {
    generarGrafico:function (desdeArchivo = true) {
        // Cargar los datos
        const datos = cargarDatos(desdeArchivo);
    
        // Separar los datos de x e y
        const x = datos.map(fila => fila[7]);
        const y = datos.map(fila => parseFloat(fila[2]));
    
        // Crear la figura
        const trace = {
            x: x,
            y: y,
            mode: 'markers',
            type: 'scatter'
        };
    
        // Diseñar el diseño del gráfico
        const layout = {
            title: 'Gráfico interactivo de temperatura real',
            xaxis: { title: 'Timestamp' },
            yaxis: { title: 'Temperatura Real (°C)' },
            hovermode: 'closest'
        };
    
        const graphOptions = {
            layout: layout,
            filename: 'grafico_interactivo',
            fileopt: 'overwrite'
        };
    
        // Guardar el gráfico en un archivo JSON
        plotly.plot([trace], graphOptions, function (err, msg) {
            if (err) return console.log(err);
            console.log(msg);
            fs.writeFileSync('grafico_interactivo.json', JSON.stringify(msg));
        });
    },
    
     mostrarGrafico:function(res, req) {
        // No es necesario abrir el archivo en el navegador cuando se genera en Node.js
        // console.log("El archivo del gráfico interactivo se ha generado correctamente.");
        res.render('index', { title: 'Express' });
    }

}




// module.exports = { generarGrafico, mostrarGrafico };
