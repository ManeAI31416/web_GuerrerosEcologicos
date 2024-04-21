document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.getElementById('formulario');
    const enviarBtn = document.querySelector('button[type="submit"]');
    const siguiente = document.getElementById('siguiente');
    const siBtn = document.getElementById('si');
    const noBtn = document.getElementById('no');

    formulario.addEventListener('submit', function(event) {
        event.preventDefault();

        const respuesta = document.getElementById('respuesta').value;

        // Verificar si el cuadro de texto está vacío
        if (!respuesta.trim()) {
            alert('El campo debe contener información');
            return;
        }

        enviarBtn.disabled = true; // Deshabilitar el botón de enviar

        // Agregar la respuesta del usuario al chatbox
        const chatbox = document.getElementById('chatbox');
        const mensaje = document.createElement('div');
        mensaje.classList.add('message');
        mensaje.classList.add('sent');
        mensaje.textContent = respuesta;
        chatbox.appendChild(mensaje);

        // Limpiar el cuadro de texto
        document.getElementById('respuesta').value = '';

        // Mostrar el mensaje de "Esperando respuesta de guecologicos..."
        const mensajeEspera = document.createElement('div');
        mensajeEspera.classList.add('message');
        mensajeEspera.classList.add('received');
        mensajeEspera.textContent = 'Esperando respuesta de guecologicos...';
        chatbox.appendChild(mensajeEspera);

        // Ocultar el formulario después de enviar la respuesta
        formulario.style.display = 'none';

        fetch('/procesar', {
            method: 'POST',
            body: new URLSearchParams({
                respuesta: respuesta
            }),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(response => response.text())
        .then(retroalimentacion => {
            // Eliminar el mensaje de "Esperando respuesta de guecologicos..."
            chatbox.removeChild(mensajeEspera);

            // Mostrar la retroalimentación en el chat
            const mensajeRetro = document.createElement('div');
            mensajeRetro.classList.add('message');
            mensajeRetro.classList.add('received');
            mensajeRetro.textContent = retroalimentacion;
            chatbox.appendChild(mensajeRetro);

            // Mostrar el div "siguiente"
            siguiente.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });

    siBtn.addEventListener('click', function() {
        // Recargar la página para obtener una nueva pregunta
        location.reload();
    });

    noBtn.addEventListener('click', function() {
        // Redirigir al usuario a la página de agradecimiento
        window.location.href = '/end.html';
    });
});
