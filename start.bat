@echo off
title CyberSec Awareness Training Website
color 0A
chcp 65001 >nul

echo.
echo  ============================================================
echo    CYBERSECURITY AWARENESS TRAINING WEBSITE
echo    Backend : Python + Flask + SQLAlchemy
echo    Frontend: HTML5 + CSS3 + Bootstrap 5 + JavaScript
echo  ============================================================
echo.

if not exist "venv\" (
    echo  [SETUP] Virtual environment not found. Setting up...
    python -m venv venv
    if errorlevel 1 (
        echo  [ERROR] Python not found! Install from https://www.python.org/
        pause
        exit /b 1
    )
    echo  [SETUP] Installing Python packages...
    venv\Scripts\pip.exe install -r requirements.txt
    echo.
)

if not exist "database\" mkdir database

if not exist "database\cybersecurity.db" (
    echo  [SETUP] First run detected - seeding database...
    set PYTHONIOENCODING=utf-8
    venv\Scripts\python.exe backend\seed_data.py
    echo.
)

echo  [OK]  Backend  --^> backend\ (Flask + Python + SQLAlchemy)
echo  [OK]  Frontend --^> frontend\ (HTML5 + CSS3 + JS + Bootstrap 5)
echo  [OK]  Database --^> database\cybersecurity.db (SQLite)
echo.
echo  [INFO] Starting server at: http://localhost:5000
echo  [INFO] Press CTRL+C to stop.
echo  ============================================================
echo.

set PYTHONIOENCODING=utf-8
venv\Scripts\python.exe backend\app.py

echo.
echo  Server stopped. Press any key to exit.
pause >nul
