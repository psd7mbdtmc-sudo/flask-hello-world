import os
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8938576468:AAEg4RFPYbKYav4nLZJuUFwQFgYd5OEimY8"
INVITE_COUNT = 10
CHANNEL_USERNAME = "@ALGOSPOR_PRO"
BOT_USERNAME = "AlgoLiveSportEntryBot"

@app.route('/')
def home():
    return f"Bot is running successfully for {CHANNEL_USERNAME}"

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        json_data = request.get_json(force=True, silent=True)
        print("Received webhook data:", json_data)
        
        if json_data and 'message' in json_data:
            message = json_data['message']
            chat_id = message['chat']['id']
            text = message.get('text', '')
            
            if text.startswith('/start'):
                ref_link = f"https://t.me/{BOT_USERNAME}?start={chat_id}"
                response_text = (
                    f"مرحباً بك في قناة {CHANNEL_USERNAME}!\n\n"
                    f"رابط الدعوة الخاص بك:\n{ref_link}\n\n"
                    f"دعواتك: 0/{INVITE_COUNT}\n"
                    f"قم بدعوة {INVITE_COUNT} أشخاص للحصول على رابط القناة."
                )
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
                payload = {
                    "chat_id": chat_id,
                    "text": response_text
                }
                res = requests.post(url, json=payload)
                print("Telegram API response:", res.text)
                
    except Exception as e:
        print("Error processing webhook:", e)
        
    return "OK", 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

