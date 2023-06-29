document.addEventListener('DOMContentLoaded', () => {
    const menuOptions = document.querySelectorAll('#menu a');
    menuOptions.forEach(option => {
      option.addEventListener('click', (event) => {
        event.preventDefault();
        const action = option.dataset.action;
        socket.send(JSON.stringify({ type: 'menu', action }));
      });
    });
  });
  