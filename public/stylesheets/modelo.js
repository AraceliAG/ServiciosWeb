const fs = require('fs');

function cargarDatos(desdeArchivo) {
    let datos = [];
    if (desdeArchivo) {
        const contenidoArchivo = fs.readFileSync('datos_exportados.csv', 'utf8');
        const lineas = contenidoArchivo.split('\n');
        // Ignorar la primera línea si contiene encabezados
        lineas.shift();
        lineas.forEach(linea => {
            const valores = linea.trim().split(',');
            datos.push(valores.map(valor => valor.trim().replace('°', '')));
        });
    } else {
        // Datos de ejemplo si no se carga desde un archivo
        datos = [
            ["Guadalajara, Jalisco, Mexico Weather Conditions", "70 °F", "68°", "51", "moderate", "0", "Expect dry conditions for the next 6 hours.", "2024-03-07 20:33:18"],
            ["Guadalajara, Jalisco, Mexico Weather Conditions", "70 °F", "68°", "51", "moderate", "0", "Expect dry conditions for the next 6 hours.", "2024-03-07 20:35:44"],
            ["Guadalajara, Jalisco, Mexico Weather Conditions", "70 °F", "68°", "51", "moderate", "0", "Expect dry conditions for the next 6 hours.", "2024-03-07 20:38:03"],
            ["Guadalajara, Jalisco, Mexico Weather Conditions", "70 °F", "68°", "51", "moderate", "0", "Expect dry conditions for the next 6 hours.", "2024-03-07 20:40:23"]
        ];
    }
    return datos;
}

module.exports = cargarDatos;

