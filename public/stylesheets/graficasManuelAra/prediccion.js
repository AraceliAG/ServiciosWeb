function calcular() {
    // Obtener los valores ingresados por el usuario
    var maxTemp = parseFloat(document.getElementById("maxTemp").value);
    var minTemp = parseFloat(document.getElementById("minTemp").value);
    var precipitacion = parseFloat(document.getElementById("prec").value);
    var lluvia = parseFloat(document.getElementById("lluv").value);
    var precHoras = parseFloat(document.getElementById("precHoras").value);
    var viento = parseFloat(document.getElementById("Aire").value);


    var tempSiguienteDia = (maxTemp + minTemp) / 2 + lluvia * 0.1 - viento * 0.5 + precHoras * 0.3;
    var maxTempSiguienteDia = tempSiguienteDia + (Math.abs(maxTemp - minTemp) / 2) + 3.38;

 
    document.getElementById("resultado").value +=  maxTempSiguienteDia.toFixed(2) + " °C";
}
