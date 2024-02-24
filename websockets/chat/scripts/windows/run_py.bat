@echo off

REM Create a virtual environment
python -m venv backend\python\venv

REM Activate the virtual environment
CALL backend\python\venv\Scripts\activate.bat

REM Install dependencies
pip install -r backend\python\requirements.txt

REM Run the Python script
python backend\python\main.py

REM Deactivate the virtual environment and end the script
CALL backend\python\venv\Scripts\deactivate.bat

@echo on