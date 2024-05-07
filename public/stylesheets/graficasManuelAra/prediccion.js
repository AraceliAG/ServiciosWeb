function limpiar() {
    document.getElementById("maxTemp").value = "";
    document.getElementById("minTemp").value = "";
    document.getElementById("lluv").value = "";
    document.getElementById("precHoras").value = "";
    document.getElementById("Aire").value = "";
}

function calcular() {
    // Obtener los valores ingresados por el usuario
    var maxTemp = parseFloat(document.getElementById("maxTemp").value);
    var minTemp = parseFloat(document.getElementById("minTemp").value);
    var lluvia = parseFloat(document.getElementById("lluv").value);
    var precHoras = parseFloat(document.getElementById("precHoras").value);
    var viento = parseFloat(document.getElementById("Aire").value);

    var tempSiguienteDia = (maxTemp + minTemp) / 2 + lluvia * 0.1 - viento * 0.5 + precHoras * 0.3;
    var maxTempSiguienteDia = tempSiguienteDia + (Math.abs(maxTemp - minTemp) / 2) + 3.38;

    // Asignar el resultado directamente al elemento resultado
    document.getElementById("resultado").value = maxTempSiguienteDia.toFixed(2) + " °C";

    // Limpiar los campos después de calcular
    limpiar();
}
