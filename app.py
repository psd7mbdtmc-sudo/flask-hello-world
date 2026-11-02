from flask import Flask
app = Flask(__name__)
from flask import Flask
app = Flask(__name__)

INVITE_COUNT = 10

@app.route('/')
def hello_world():
    return f'Bot is active! Required invites: {INVITE_COUNT}'

@app.route('/')
def hello_world():
    return 'Hello, World!'
