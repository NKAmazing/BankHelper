let url = `ws://${window.location.host}/ws/socket-server/`;

const socket = new WebSocket(url);

socket.onopen = function(event) {
    console.log('WebSocket is connected.');
}

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
  
    console.log("Data: ", data);
  
    if (data.type === 'chat') {
      const messageContainer = document.getElementById('messages');
      const messageElement = document.createElement('div');
      messageElement.innerHTML = `<p>${data.message}</p>`;
      messageContainer.appendChild(messageElement);
    }
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
