let url = `ws://${window.location.host}/ws/socket-server/`;

const socket = new WebSocket(url);

socket.onopen = function(event) {
    console.log('WebSocket is connected.');
}

// Function to scroll to the bottom of the chat log
function scrollToBottom() {
    const chatLog = document.getElementById('message_box');
    chatLog.scrollTop = chatLog.scrollHeight;
};

// Function to handle the menu click
function handleMenuClick(e) {
    const action = e.target.getAttribute('data-action');
    if (action) {
        // Call the function with the specified action
        if (action === 'get_account_info') {
            // Remove the hidden class from the input and button
            document.getElementById('gai_account_id_input').classList.remove('hidden');
            document.getElementById('get_account_info_button').classList.remove('hidden');
            const getAccountInfoButton = document.getElementById('get_account_info_button');
            getAccountInfoButton.addEventListener('click', function() {
                const accountId = document.getElementById('gai_account_id_input').value;
                if (accountId) {
                    // Send the data to the WebSocket server
                    socket.send(JSON.stringify({
                        'action': 'get_account_info',
                        'account_id': accountId
                    }));
                } else {
                    alert("You must enter an account ID!");
                }
            });
        } else if (action === 'make_transaction') {
            // Remove the hidden class from the input and button
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
                    // Send the data to the WebSocket server
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
            // Remove the hidden class from the input and button
            document.getElementById('stl_account_id_input').classList.remove('hidden');
            document.getElementById('show_transactions_list_button').classList.remove('hidden');
            const showTransactionsListButton = document.getElementById('show_transactions_list_button');
            showTransactionsListButton.addEventListener('click', function() {
                const accountId = document.getElementById('stl_account_id_input').value;
                if (accountId) {
                    // Send the data to the WebSocket server
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
    // Handle the response from the server
    if (data.action === 'get_account_info') {
        const accountInfo = data.account_info;
        const formattedData = `
        <div class="message received">
            <p>Account Info:</p>
            <p>Account Number: ${accountInfo.account_number}</p>
            <p>Balance: ${accountInfo.balance.toFixed(2)}</p>
            <p>Bank: ${accountInfo.bank || 'N/A'}</p>
        </div>
        `;
        document.getElementById('result-container').innerHTML = formattedData;
    } else if (data.action === 'make_transaction') {
        const response = data.transaction_info;
        const formattedData = `
        <div class="message received">
            <p>${response}</p>
        </div>
        `;
        document.getElementById('result-container').innerHTML = formattedData;
    } else if (data.action === 'show_transactions_list') {
        const transactionsList = data.transactions_list;
        let formattedData = `
        <div class="message received">
            <p>Transaction List:</p>
        `;
        
        for (let i = 0; i < transactionsList.length; i++) {
        const transaction = transactionsList[i];
        formattedData += `
            <p>Amount: ${transaction.amount}</p>
            <p>Date: ${transaction.date}</p>
            <p>Status: ${transaction.status}</p>
            <p>Source Account: ${transaction.source_account}</p>
            <p>Destination Account: ${transaction.destination_account}</p>
            <hr>
        `;
        }
        
        formattedData += '</div>';
        document.getElementById('result-container').innerHTML = formattedData;
    }
}

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