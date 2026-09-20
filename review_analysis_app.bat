@echo off
setlocal

echo [INFO] Searching for Python installation...

:: Получаем путь к Python
for /f "delims=" %%i in ('where python 2^>nul') do (
    set PYTHON_PATH=%%i
)

:: Проверяем, найден ли Python
if not defined PYTHON_PATH (
    echo [ERROR] Python is not installed or not found in PATH!
    echo [INFO] Please install Python from https://www.python.org/downloads/
    start https://www.python.org/downloads/
    pause
    exit /b
)

echo [INFO] Found Python at: %PYTHON_PATH%

echo [INFO] Setting up virtual environment...
if not exist "venv" (
    %PYTHON_PATH% -m venv venv
    echo [INFO] Virtual environment created.
)

echo [INFO] Activating environment and installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo [INFO] Starting the application...
streamlit run review_analysis_app.py

pause
