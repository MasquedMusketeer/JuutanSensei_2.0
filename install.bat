@echo off
setlocal

rem Get the directory of the batch file (pyMenu folder)
set "pyMenu_dir=%~dp0"

rem Navigate to the Data folder
cd /d "%pyMenu_dir%Data"

rem Run the Python script with the start command
start "JutanSensei" python "dependenciesChkModule.py"