@echo off
set CHROMEDRIVER=%1

call venv\Scripts\activate.bat
set PATH=%PATH%;%CHROMEDRIVER%
echo %PATH%
pytest test_app.py
set EXIT_CODE=%ERRORLEVEL%

if %EXIT_CODE%==0 (
    exit /b 0
) else (
    exit /b 1
)