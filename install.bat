@echo off
REM Installation script for Badge Access System (Windows)

echo =========================================
echo Badge Access System - Installation Script
echo =========================================

REM Check Python version
echo Checking Python version...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
python --version
echo Python found

REM Create virtual environment
echo.
echo Creating virtual environment...
if exist venv (
    echo Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo Virtual environment created
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo Virtual environment activated

REM Upgrade pip
echo.
echo Upgrading pip...
python -m pip install --upgrade pip --quiet
echo pip upgraded

REM Install requirements
echo.
echo Installing required packages...
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install packages
    pause
    exit /b 1
)
echo All packages installed

REM Initialize database
echo.
echo Initializing database...
python -c "from Schema_exec import extend_schema; extend_schema()" 2>nul
echo Database initialized

REM Ask about sample data
echo.
set /p load_sample="Do you want to load sample data? (y/n): "
if /i "%load_sample%"=="y" (
    if exist accesdb_seed_data.sql (
        sqlite3 accessdb.db < accesdb_seed_data.sql 2>nul
    )
    if exist check_in_seed_data.sql (
        sqlite3 accessdb.db < check_in_seed_data.sql 2>nul
    )
    echo Sample data loaded
)

echo.
echo =========================================
echo Installation Complete!
echo =========================================
echo.
echo To run the application:
echo   1. Activate the virtual environment: venv\Scripts\activate
echo   2. Run the application: python building-access.py
echo.
pause