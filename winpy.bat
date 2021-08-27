@echo off
set "MYHOME = %~dp0\..\.."
call "%MYHOME%\WPy64-3950\scripts\env_for_icons.bat"  
cmd.exe "/k %MYHOME%\cmder\vendor\init.bat