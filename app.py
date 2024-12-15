from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from googletrans import Translator
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(24).hex())
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='gevent')
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    message = data['message']
    source_lang = data['source_lang']
    target_lang = data['target_lang']
    
    try:
        # Traduire le message
        translation = translator.translate(
            message,
            src=source_lang,
            dest=target_lang
        )
        
        # Envoyer le message original et traduit à tous les clients
        emit('receive_message', {
            'original': message,
            'translated': translation.text,
            'source_lang': source_lang,
            'target_lang': target_lang
        }, broadcast=True)
    except Exception as e:
        emit('error', {'message': str(e)})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 10000))
    socketio.run(app, 
                host='0.0.0.0',
                port=port)
