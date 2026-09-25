@echo off
title CyberSec Awareness Training - LIVE Public Server
color 0B
chcp 65001 >nul

echo.
echo ======================================================================
echo    CYBERSECURITY AWARENESS TRAINING - LIVE PUBLIC SERVER
echo    Frontend: HTML5 + CSS3 + Bootstrap 5 + JavaScript
echo    Backend : Python Flask + SQLAlchemy + Neon Cloud PostgreSQL
echo ======================================================================
echo.

if not exist "venv\" (
    echo [ERROR] Virtual environment not found. Please run start.bat first.
    pause
    exit /b 1
)

if not exist "cloudflared.exe" (
    echo [ERROR] cloudflared.exe not found in this folder!
    pause
    exit /b 1
)

echo [1/2] Starting local Flask backend server...
start /b venv\Scripts\python.exe backend\app.py

timeout /t 3 >nul

echo.
echo [2/2] Starting public secure HTTPS live tunnel...
echo ======================================================================
echo Look for your live link below (e.g. https://xxxx.trycloudflare.com):
echo ======================================================================
echo.

cloudflared.exe tunnel --url http://127.0.0.1:5000

pause
