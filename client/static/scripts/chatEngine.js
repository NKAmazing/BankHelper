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

        function handleMenuClick(e) {
            const action = e.target.getAttribute('data-action');
            if (action) {
                // Llamar a la función correspondiente según la acción seleccionada
                if (action === 'get_account_info') {
                    // Lógica para mostrar el formulario o solicitar datos para obtener información de la cuenta
                    const accountId = prompt("Please enter your account ID:");
                    if (accountId) {
                        // Enviar los datos al servidor WebSocket
                        socket.send(JSON.stringify({
                            'action': 'get_account_info',
                            'account_id': accountId
                        }));
                    } else {
                        alert("You must enter an account ID!");
                    }

                } else if (action === 'make_transaction') {
                    // Lógica para mostrar el formulario o solicitar datos para realizar una transacción
                    const accountId = prompt("Please enter your account ID:");
                    const amount = prompt("Please enter the amount to transfer:");
                    const destinationAccountId = prompt("Please enter the destination account ID:");
                    if (accountId && amount && destinationAccountId) {
                        // Enviar los datos al servidor WebSocket
                        socket.send(JSON.stringify({
                            'action': 'make_transaction',
                            'account_id': accountId,
                            'amount': amount,
                            'destination_account_id': destinationAccountId
                        }));
                    } else {
                        alert("You must enter all the data!");
                    }

                } else if (action === 'show_transactions_list') {
                    // Lógica para mostrar la lista de transacciones
                    const accountId = prompt("Please enter your account ID:");
                    if (accountId) {
                        // Enviar los datos al servidor WebSocket
                        socket.send(JSON.stringify({
                            'action': 'show_transactions_list',
                            'account_id': accountId
                        }));
                    } else {
                        alert("You must enter an account ID!");
                    }
                }                
            }
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