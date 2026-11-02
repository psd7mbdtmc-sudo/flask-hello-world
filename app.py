import os
from flask import Flask, request
import requests

app = Flask(__name__)

# التوكن الخاص بك مدمج هنا
BOT_TOKEN = "8938576468:AAEg4RFPYbKYav4nLZJuUFwQFgYd5OEimY8"
INVITE_COUNT = 10
CHANNEL_USERNAME = "@ALGOSPOR_PRO"
BOT_USERNAME = "AlgoLiveSportEntryBot"

@app.route('/')
def home():
    return f"Bot is running successfully for {CHANNEL_USERNAME}"

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()
    if json_data and 'message' in json_data:
        message = json_data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        
        if text.startswith('/start'):
            # رابط الإحالة الخاص بالمستخدم
            ref_link = f"https://t.me/{BOT_USERNAME}?start={chat_id}"
            
            # النص المحدث بالطلب الجديد (10 أشخاص)
            response_text = (
                f"مرحباً بك في قناة {CHANNEL_USERNAME}!\n\n"
                f"رابط الدعوة الخاص بك:\n{ref_link}\n\n"
                f"دعواتك: 0/{INVITE_COUNT}\n"
                f"قم بدعوة {INVITE_COUNT} أشخاص للحصول على رابط القناة."
            )
            
            # إرسال الرسالة عبر تليجرام API
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": response_text
            }
            requests.post(url, json=payload)
            
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
