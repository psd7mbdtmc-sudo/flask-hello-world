from flask import Flask, request

app = Flask(__name__)

# المتغيرات الأساسية المطلوبة
INVITE_COUNT = 10
CHANNEL_USERNAME = "@ALGOSPOR_PRO"

@app.route('/')
def home():
    return f"Bot is running successfully for {CHANNEL_USERNAME}"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    
    if data and 'message' in data:
        message = data['message']
        chat_id = message['chat']['id']
        text = message.get('text', '')
        
        if text.startswith('/start'):
            # النص البرمجي المحدث بالكامل ليطلب 10 أشخاص
            response_text = (
                f"مرحباً بك في قناة {CHANNEL_USERNAME}!\n\n"
                f"رابط الدعوة الخاص بك:\n"
                f"https://t.me/AlgoLiveSportEntryBot?start={chat_id}\n\n"
                f"دعواتك: 0/{INVITE_COUNT}\n"
                f"قم بدعوة {INVITE_COUNT} أشخاص للحصول على رابط القناة."
            )
            # هنا يتم إرسال الرد عبر تيليجرام API (يمكنك ربطه بالتوكن الخاص بك)
            
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
