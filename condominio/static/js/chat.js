const contactsList = document.getElementById('contacts-list');
const recadoForm = document.getElementById('recado-form');
const recadoInput = document.getElementById('recado-input');
const fileInput = document.getElementById('file-input');
const messageList = document.getElementById('message-list');

let selectedContactId = null;

contactsList.addEventListener('click', (event) => {
    if (event.target.tagName === 'LI') {
        selectedContactId = event.target.dataset.id;
        document.getElementById('contact-name').textContent = event.target.textContent;
    }
});

recadoForm.addEventListener('submit', (event) => {
    event.preventDefault();

    if (selectedContactId === null) {
        alert('Selecione um contato para enviar a mensagem!');
        return;
    }

    const formData = new FormData();
    const newRecado = recadoInput.value.trim();
    const file = fileInput.files[0];

    if (newRecado !== '') {
        formData.append('text', newRecado);
        formData.append('sent', true);
    }
    if (file) {
        formData.append('file', file);
    }

    fetch(`http://localhost:3000/api/messages/${selectedContactId}`, {
        method: 'POST',
        body: formData
    })
    .then(() => {
        recadoInput.value = '';
        fileInput.value = '';
        loadRecados();
    });
});

function loadRecados() {
    fetch(`http://localhost:3000/api/messages/${selectedContactId}`)
        .then(response => response.json())
        .then(data => {
            messageList.innerHTML = '';
            data.forEach((recado, index) => {
                const recadoElement = document.createElement('div');
                recadoElement.className = 'recado';
                if (recado.text) {
                    recadoElement.innerHTML += `<p>${recado.text}</p>`;
                }
                if (recado.file_url) {
                    recadoElement.innerHTML += `<p><a href="${recado.file_url}" target="_blank">Ver Arquivo</a></p>`;
                }
                recadoElement.innerHTML += `<button onclick="removeRecado(${index})">Remover</button>`;
                messageList.appendChild(recadoElement);
            });
        });
}

// Load messages for the selected contact when the page loads
loadRecados();