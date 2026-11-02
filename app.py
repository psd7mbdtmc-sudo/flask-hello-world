import os
from flask import Flask, request
import requests

app = Flask(__name__)

TOKEN = "8938576468:AAEg4RFPYbKYav4nLZJuUFwQFgYd5OEimY8"
TELEGRAM_URL = f"https://api.telegram.org/bot{TOKEN}"

@app.route('/')
def home():
    print(">>> BOT_READY_NOW <<<")
    return "Bot is running successfully"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    if data and 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        if text == '/start':
            # رسالة الترحيب ورابط الدعوة
            welcome_message = (
                "أهلاً بك في القناة! 📊⚽\n\n"
                "لكي تتمكن من الانضمام إلى القسم الخاص والحصول على رابط الدخول، يُشترط دعوة 10 أشخاص عبر رابط الدعوة الخاص بك. بعد الانتهاء سوف يصلك رابط القناة للدخول.\n\n"
                "رابط الدعوة الخاص بك:\n"
                "https://t.me/ALGOSPORTPRO"
            )
            
            # إرسال الرسالة عبر تيليجرام
            send_url = f"{TELEGRAM_URL}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": welcome_message
            }
            requests.post(send_url, json=payload)
            
    return "ok", 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
