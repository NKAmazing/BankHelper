const socket = new WebSocket('ws://localhost:8000/ws/');

socket.onopen = function(event) {
    console.log('WebSocket is connected.');
}

socket.onmessage = function(event) {
    // Convertir el mensaje JSON a objeto JavaScript
    const message = JSON.parse(event.data);

    // Utilizar los datos para actualizar el contenido del template
    document.querySelector('#chat-messages').innerHTML += message.message;
}

socket.onclose = function(event) {
    console.log('WebSocket is closed.');
}
