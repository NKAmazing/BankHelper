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