import React, { useState } from 'react';

const ChatComponent = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí puedes realizar acciones como enviar el mensaje al backend o manejar la lógica deseada
    setMessages([...messages, message]);
    setMessage('');
  };

  return (
    <div>
      <div id="messages">
        {messages.map((msg, index) => (
          <div key={index}>{msg}</div>
        ))}
      </div>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          id="message-input"
          autoComplete="off"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
};

export default ChatComponent;
