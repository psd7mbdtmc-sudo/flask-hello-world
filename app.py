from flask import Flask
app = Flask(__name__)

INVITE_COUNT = 10

@app.route('/')
def hello_world():
    return f'مرحبا بك معنا . في قناه @ALGOSPOR_PRO هنالك شرط بسيط لدخول. اضف {INVITE_COUNT} اشخاص ليتم قبولك'

