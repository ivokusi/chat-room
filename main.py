from flask import Flask, render_template, request, session, redirect
from flask_socketio import SocketIO, join_room, leave_room, send
from string import ascii_uppercase
from dotenv import load_dotenv
import random
import os

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

if __name__ == "__main__":
    socketio.run(app, debug=True)
