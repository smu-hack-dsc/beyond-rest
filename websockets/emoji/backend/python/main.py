from flask import Flask, request
from flask_socketio import SocketIO, join_room, emit
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Configure SocketIO with CORS allowed
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return "Chat Server is running!"


@socketio.on('connection')
def handle_connect():
    print('A user connected')


@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')


@socketio.on('joinRoom')
def handle_join_room(room_id):
    join_room(room_id)
    print(f'User joined room: {room_id}')


@socketio.on('chatMessage')
def handle_chat_message(message):
    emit('receiveMessage', message, broadcast=True)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 3000))
    socketio.run(app, host='0.0.0.0', port=port)
