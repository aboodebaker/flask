from flask import Flask, jsonify
import os
from claude_api import Client

app = Flask(__name__)

def get_cookie():
    # Your get_cookie function remains the same
    cookie = 'sessionKey=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'
    return cookie

@app.route('/chat', methods=['POST'])
def chat():
    cookie = get_cookie()
    claude = Client(cookie)
    conversation_id = request.json.get('conversation_id')

    user_input = request.json.get('user_input')

    if user_input.lower() == 'exit':
        return jsonify({'response': "Thank you!"})

    if not conversation_id:
        conversation = claude.create_new_chat()
        conversation_id = conversation['uuid']

    response = claude.send_message(user_input, conversation_id)
    return jsonify({'response': response, 'conversation': conversation_id})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
