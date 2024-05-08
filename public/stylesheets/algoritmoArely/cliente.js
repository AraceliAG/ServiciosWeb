const websocket = new WebSocket("ws://localhost:6969");

websocket.onmessage = function (event) {
    console.log("Se recibió el mensaje:", event.data);
};

websocket.onerror = function (event) {
    console.error("Error en WebSocket:", event);
};

// Función para enviar un mensaje al servidor
async function enviarMensaje() {
    const mensaje = await obtenerMensaje();
    websocket.send(mensaje);
}

async function obtenerMensaje() {
    return new Promise((resolve, reject) => {
        const mensaje = prompt("Introduce el mensaje:");
        resolve(mensaje);
    });
}

// Manejo de la conexión WebSocket
websocket.onopen = function (event) {
    console.log("Conexión establecida.");
    enviarMensaje(); // Enviar el primer mensaje después de la conexión establecida
};

// Manejo de la desconexión WebSocket
websocket.onclose = function (event) {
    console.log("Conexión cerrada.");
};

// Escuchar eventos del teclado para enviar mensajes
process.stdin.on('data', function (data) {
    if (data.toString().trim() === "exit") {
        websocket.close();
        process.exit();
    } else {
        enviarMensaje();
    }
});
