// script.js

document.addEventListener('DOMContentLoaded', () => {
    const messagesList = document.getElementById('messages-list');
    const messageForm = document.getElementById('message-form');
    const messageInput = document.getElementById('message-input');
    const fileInput = document.getElementById('file-input');
    const residentList = document.getElementById('resident-list');
    let currentResidentId = 1; // Morador padrão selecionado

    // Atualiza a lista de mensagens para o morador atual
    function loadMessages() {
        fetch(`http://localhost:3000/api/messages/${currentResidentId}`)
            .then(response => response.json())
            .then(data => {
                messagesList.innerHTML = '';
                data.forEach((message, index) => {
                    const messageElement = document.createElement('div');
                    messageElement.className = 'message';
                    messageElement.innerHTML = `<strong>${message.sender}:</strong> `;
                    if (message.text) {
                        messageElement.innerHTML += `<p>${message.text}</p>`;
                    }
                    if (message.file_url) {
                        messageElement.innerHTML += `<p><a href="${message.file_url}" target="_blank">Ver Arquivo</a></p>`;
                    }
                    messagesList.appendChild(messageElement);
                });
            });
    }

    // Seleção de morador
    residentList.addEventListener('click', (event) => {
        if (event.target.tagName === 'LI') {
            currentResidentId = event.target.getAttribute('data-id');
            loadMessages();
        }
    });

    // Envia uma nova mensagem
    messageForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData();
        const newMessage = messageInput.value.trim();
        const file = fileInput.files[0];

        if (newMessage !== '') {
            formData.append('text', newMessage);
            formData.append('sender', 'porteiro/sindico');
        }
        if (file) {
            formData.append('file', file);
        }

        fetch(`http://localhost:3000/api/messages/${currentResidentId}`, {
            method: 'POST',
            body: formData
        })
        .then(() => {
            messageInput.value = '';
            fileInput.value = '';
            loadMessages();
        });
    });

    loadMessages();
});
