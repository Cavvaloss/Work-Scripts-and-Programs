strComputer = "."
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")
set objShell = wscript.CreateObject("wscript.shell")
	Do
	WScript.Sleep(10000)
	Set colItems = objWMIService.ExecQuery("Select * from Win32_NetworkAdapter Where Name = 'AdapterName'",,48)
	For Each objItem in colItems
		x = ObjItem.NetConnectionStatus 
		If x <> 2 Then
			intReturn = objShell.Popup("Click ""Yes"" to shutdown, or ""No"" to prevent shutdown", _
  			20, "Shutdown Computer", vbYesNo + vbInformation)

			If (intReturn = vbNo) Then
  			Wscript.Quit
			Else 
			  objShell.Run "shutdown.exe /R /t 5"
			End If
		End If
		
Next
Loop
