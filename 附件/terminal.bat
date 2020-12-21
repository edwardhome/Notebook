@echo off
:: BatchGotAdmin (Run as Admin code starts)
REM --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
echo Requesting administrative privileges...
goto UACPrompt
) else ( goto gotAdmin )
:UACPrompt
echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\getadmin.vbs"
"%temp%\getadmin.vbs"
exit /B
:gotAdmin
if exist "%temp%\getadmin.vbs" ( del "%temp%\getadmin.vbs" )
pushd "%CD%"
CD /D "%~dp0"
:: BatchGotAdmin (Run as Admin code ends)
:: Your codes should start from the following line
echo Modify setting policy
powershell.exe Set-ExecutionPolicy RemoteSigned
pause
powershell.exe Get-ExecutionPolicy
pause
echo Download the posh file .....
powershell.exe Install-Module posh-git -Scope CurrentUser
pause
echo install the oh-my-posh, please key A or Y
powershell.exe Install-Module oh-my-posh -Scope CurrentUser
pause
echo fix the powershell profile
powershell.exe Set-Content $PROFILE 'Import-Module posh-git','Import-Module oh-my-posh','Set-Theme Paradox'
echo Press any key to exit
pause >null
ECHO finish
