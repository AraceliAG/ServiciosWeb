// Obtener referencia al botón y al modal
var btnMostrarModal = document.getElementById("btnMostrarModal");
var modal = document.getElementById("modal");

// Obtener referencia al botón de cerrar el modal
var closeBtn = document.getElementById("close");

// Mostrar modal al hacer clic en el botón "Avanzado"
btnMostrarModal.onclick = function() {
    modal.style.display = "block";
}

// Ocultar modal al hacer clic en el botón de cerrar
closeBtn.onclick = function() {
    modal.style.display = "none";
}