from flask import Flask
app = Flask(__name__)

INVITE_COUNT = 10

@app.route('/')
def hello_world():
    return 'مرحباً بك معنا في قناة @ALGOSPOR_PRO'
