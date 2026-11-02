from flask import Flask, request

app = Flask(__name__)

# إعدادات القناة وشرط الدعوات الجديد
INVITE_COUNT = 10
CHANNEL_USERNAME = "@ALGOSPOR_PRO"

@app.route('/')
def hello_world():
    return f'مرحباً بك معنا في قناة {CHANNEL_USERNAME} - نظام الإحالة يعمل بنجاح (الشرط: {INVITE_COUNT} أشخاص).'

@app.route('/webhook', methods=['POST'])
def webhook():
    # هنا يتم استقبال بيانات تيليجرام ومعالجة أمر /start والعداد
    data = request.get_json()
    
    # يمكنك وضع منطق البوت هنا أو تخصيصه حسب الحاجة
    # النص المحدث الذي يظهر للمستخدم:
    # دعواتك: 0/10
    # قم بدعوة 10 أشخاص للحصول على رابط القناة.
    
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
