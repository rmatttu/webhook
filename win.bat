@echo off
cd /d %~dp0

python webhook.py

if not %errorlevel% == 0 (
  pause
)

REM vim: set fenc=cp932 ff=dos nomodified:

