from flask import Flask, jsonify, request
import os
from claude_api import Client
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_cookie():
  try:
    # Your get_cookie function remains the same
    cookie = os.environ.get('cookie')
    return cookie
  except Exception as e:
    print(e)

cookie = get_cookie()
claude = Client(cookie)

@app.route('/chat', methods=['POST'])
def chat():
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
