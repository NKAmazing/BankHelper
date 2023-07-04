import { handleMenuClick } from './clickEventManager.js';
import { handleServerResponse } from './serverManager.js';

let url = `ws://${window.location.host}/ws/socket-server/`;

const socket = new WebSocket(url);

socket.onopen = function(event) {
    console.log('WebSocket is connected.');
}

// Función para hacer scroll hacia abajo en el chat
function scrollToBottom() {
    const chatLog = document.getElementById('message_box');
    chatLog.scrollTop = chatLog.scrollHeight;
};

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const messageSent = document.getElementById('message-sent');

    console.log("Data: ", data);

    if (data.type === 'chat') {
        messageSent.innerHTML += `
            <p>${data.message}</p>
        `;

    } else {
        handleServerResponse(data);
    }

    scrollToBottom();
}      

socket.onclose = function(event) {
    console.log('WebSocket is closed.');
}

let form = document.getElementById('chat-form')
form.addEventListener('submit', (event)=> {
    event.preventDefault()
    let message = event.target.message.value
    socket.send(JSON.stringify({
        'message': message
    }))
    form.reset()
})

const menuItems = document.querySelectorAll('#menu a');
menuItems.forEach(item => {
    item.addEventListener('click', handleMenuClick);
});