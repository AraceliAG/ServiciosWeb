const websocket = new WebSocket("ws://localhost:6969");

        websocket.onmessage = function (event) {
            console.log("Se recibió el mensaje:", event.data);
            // Mostrar la respuesta durante 5 segundos
            document.getElementById("suma_total").textContent = event.data;
            setTimeout(() => {
                document.getElementById("suma_total").textContent = "";
            }, 5000); // 5000 milisegundos = 5 segundos
        };

        websocket.onerror = function (event) {
            console.error("Error en WebSocket:", event);
        };

        document.getElementById("formulario").addEventListener("submit", function(event) {
            event.preventDefault(); // Evitar que el formulario se envíe automáticamente

            const temp_max = parseFloat(document.getElementById("temp_max").value);
            const temp_min = parseFloat(document.getElementById("temp_min").value);
            const precp = parseFloat(document.getElementById("precp").value);
            const precp_h = parseFloat(document.getElementById("precp_h").value);
            const viento = parseFloat(document.getElementById("viento").value);
            
            // Calcular la suma total
            const sumaTotal = temp_max + temp_min + precp + precp_h + viento;

            // Mostrar la suma total en el campo correspondiente
            document.getElementById("suma_total").textContent = "Calculando...";

            // Enviar los datos al servidor como un mensaje JSON
            const datosFormulario = { temp_max, temp_min, precp, precp_h, viento };
            const mensaje = JSON.stringify(datosFormulario);
            websocket.send(mensaje);
        });

        // Manejo de la conexión WebSocket
        websocket.onopen = function (event) {
            console.log("Conexión establecida.");
        };

        // Manejo de la desconexión WebSocket
        websocket.onclose = function (event) {
            console.log("Conexión cerrada.");
        };