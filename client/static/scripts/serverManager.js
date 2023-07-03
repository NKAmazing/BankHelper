function handleServerResponse(data) {
    if (data.action === 'get_account_info') {
        document.getElementById('result-container').textContent = data.result;
    } else if (data.action === 'make_transaction') {
        document.getElementById('result-container').textContent = data.result;
    } else if (data.action === 'show_transactions_list') {
        document.getElementById('result-container').textContent = data.result;
    }
  }