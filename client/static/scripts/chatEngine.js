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
                    document.getElementById('gai_account_id_input').classList.remove('hidden');
                    document.getElementById('get_account_info_button').classList.remove('hidden');
                    const getAccountInfoButton = document.getElementById('get_account_info_button');
                    getAccountInfoButton.addEventListener('click', function() {
                        const accountId = document.getElementById('gai_account_id_input').value;
                        if (accountId) {
                            // Enviar los datos al servidor WebSocket
                            socket.send(JSON.stringify({
                                'action': 'get_account_info',
                                'account_id': accountId
                            }));
                        } else {
                            alert("You must enter an account ID!");
                        }
                    });
                } else if (action === 'make_transaction') {
                    document.getElementById('mt_account_id_input').classList.remove('hidden');
                    document.getElementById('mt_amount_input').classList.remove('hidden');
                    document.getElementById('mt_destination_account_id_input').classList.remove('hidden');
                    document.getElementById('make_transaction_button').classList.remove('hidden');
                    const makeTransactionButton = document.getElementById('make_transaction_button');
                    makeTransactionButton.addEventListener('click', function() {
                        const accountId = document.getElementById('mt_account_id_input').value;
                        const amount = document.getElementById('mt_amount_input').value;
                        const destinationAccountId = document.getElementById('mt_destination_account_id_input').value;
                        if (accountId && amount && destinationAccountId) {
                            // Enviar los datos al servidor WebSocket
                            socket.send(JSON.stringify({
                                'action': 'make_transaction',
                                'account_id': accountId,
                                'amount': amount,
                                'destination_account_id': destinationAccountId
                            }));
                        } else {
                            alert("You must enter all the required data!")
                        }
                    });

                } else if (action === 'show_transactions_list') {
                    document.getElementById('stl_account_id_input').classList.remove('hidden');
                    document.getElementById('show_transactions_list_button').classList.remove('hidden');
                    const showTransactionsListButton = document.getElementById('show_transactions_list_button');
                    showTransactionsListButton.addEventListener('click', function() {
                        const accountId = document.getElementById('stl_account_id_input').value;
                        if (accountId) {
                            // Enviar los datos al servidor WebSocket
                            socket.send(JSON.stringify({
                                'action': 'show_transactions_list',
                                'account_id': accountId
                            }));
                        } else {
                            alert("You must enter an account ID!");
                        }
                    });
                }                
            }
        }

        function handleServerResponse(data) {
            // Verificar el tipo de respuesta recibida
            if (data.action === 'get_account_info') {
                // Manejar la respuesta para la acción 'get_account_info'
                // Puedes acceder al resultado con data.result
                // console.log('Resultado de get_account_info:', data.result);
                // Aquí puedes actualizar el contenido del template para mostrar el resultado en el lugar correspondiente.
                // Por ejemplo, puedes seleccionar un elemento en el DOM y establecer su contenido con el resultado:
                document.getElementById('result-container').textContent = data.result;
            } else if (data.action === 'make_transaction') {
                // Manejar la respuesta para la acción 'make_transaction'
                // Puedes acceder al resultado con data.result
                // console.log('Resultado de make_transaction:', data.result);
                // Actualizar el contenido del template con el resultado
                document.getElementById('result-container').textContent = data.result;
            } else if (data.action === 'show_transactions_list') {
                // Manejar la respuesta para la acción 'show_transactions_list'
                // Puedes acceder al resultado con data.result
                // console.log('Resultado de show_transactions_list:', data.result);
                // Actualizar el contenido del template con el resultado
                document.getElementById('result-container').textContent = data.result;
            }
            // Asegúrate de manejar todos los demás casos o acciones posibles.
        }

        socket.onmessage = function(event) {
            const data = JSON.parse(event.data);
        
            console.log("Data: ", data);
        
            if (data.type === 'chat') {
                const messageContainer = document.getElementById('messages');
                const messageElement = document.createElement('div');
                messageElement.innerHTML = `<p>${data.message}</p>`;
                messageContainer.appendChild(messageElement);
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