@echo off
title PixelTrigger Pro - Setup
echo.
echo =========================================
echo    PixelTrigger Pro - Quick Setup
echo =========================================
echo.

echo [1/3] Creating virtual environment...
python -m venv .venv
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    echo Please ensure Python 3.7+ is installed
    pause
    exit /b 1
)

echo [2/3] Installing dependencies...
".venv\Scripts\pip.exe" install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [3/3] Setup complete!
echo.
echo =========================================
echo Setup completed successfully!
echo.
echo To run PixelTrigger Pro:
echo - Double-click 'run_pixeltrigger.bat'
echo - Or run: python main.py
echo =========================================
echo.
pause
