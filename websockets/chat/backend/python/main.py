from flask import Flask, request
from flask_socketio import SocketIO, join_room, emit
from flask_cors import CORS

app = Flask(__name__)
# Allow all origins with CORS
CORS(app)
# Initialize SocketIO with CORS allowed for all origins
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/')
def index():
    return "Chat Server is running!"


@socketio.on('connect')
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
    # Use port 3000 or the one set in the 'PORT' environment variable
    socketio.run(app, host='0.0.0.0', port=3000, debug=True)
