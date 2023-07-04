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

async function getBankName(bankId) {
    console.log("Getting bank name for bank ID:", bankId);
    try {
      const response = await fetch(`http://localhost:8000/bank/get/${bankId}`);
      const bankData = await response.json();
      return bankData.bank_name;
    } catch (error) {
      console.error('Error al obtener el nombre del banco:', error);
      return 'N/A';
    }
}
  

async function handleServerResponse(data) {
    console.log("Handling server response:", data);

    if (data.action === 'get_account_info') {
        const accountInfo = data.account_info;
        console.log("BANCO: ", accountInfo.bank)
        const bankName = await getBankName(accountInfo.bank);
        const formattedData = `
        <div class="message received">
            <p>Account Info:</p>
            <p>Account Number: ${accountInfo.account_number}</p>
            <p>Balance: ${accountInfo.balance.toFixed(2)}</p>
            <p>Bank: ${bankName || 'N/A'}</p>
        </div>
        `;
        document.getElementById('result-container').innerHTML = formattedData;
    } else if (data.action === 'make_transaction') {
        document.getElementById('result-container').textContent = JSON.stringify(data.result);
    } else if (data.action === 'show_transactions_list') {
        document.getElementById('result-container').textContent = JSON.stringify(data.result);
    }
}

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const messageSent = document.getElementById('message-sent');
    console.log("HOLA DESDE EL ONMESSAGE")
    console.log("Data: ", data);

    if (data.type === 'chat') {
        console.log("HOLA DESDE EL IF")
        messageSent.innerHTML += `
            <p>${data.message}</p>
        `;

    } else {
        console.log("HOLA DESDE EL ELSE")
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