@app.route('/api/messages/<int:contact_id>', methods=['GET'])
def get_messages(contact_id):
    return jsonify(messages.get(contact_id, []))

@app.route('/api/messages/<int:contact_id>', methods=['POST'])
def post_message(contact_id):
    if 'file' in request.files:
        file = request.files['file']
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Adiciona o recado com o caminho do arquivo
        messages[contact_id].append({'file_url': file_path, 'sent': True})
        return jsonify({'success': True, 'file_url': file_path})

    else:
        data = request.form
        text = data.get('text')
        sent = data.get('sent') == 'true'

        if contact_id not in messages:
            messages[contact_id] =