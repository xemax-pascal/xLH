@echo off
REM execute: setup_modules.bat
REM execute: setup_modules.bat venv
REM execute: setup_modules.bat update
setlocal
cls
REM ==================================================
cd /d %~dp0
set script_dir=%cd%
set base_dir=%cd%
set venv_dir=%cd%\venv
set python_path=C:\Python\python_portable_31011_01_02\python_31011\python.exe
set mkdocs_insiders_path="D:\Python\mkdocs-material-insiders"
echo script_dir = %script_dir%
echo base_dir = %base_dir%
echo venv_dir = %venv_dir%
echo python_path = %python_path%
echo mkdocs_insiders_path = %mkdocs_insiders_path%
REM ==================================================
cd /d "%base_dir%"
set arg_venv=%1
REM echo %delete%
REM ==================================================
if "%arg_venv%"=="venv" (
    rd /s/q "%venv_dir%"
    REM rd /s/q "%base_dir%\.idea"
    if exist "%~dp0%venv" (
        echo =========================================
        echo venv konnte nicht gelöscht werden!
        echo =========================================
    ) else (
        echo =========================================
        echo Initialisierung der virtuellen Umgebung
        echo =========================================
        "%python_path%" -m venv venv
        "%venv_dir%\Scripts\python.exe" -m pip install --upgrade pip
        "%venv_dir%\Scripts\pip.exe" install poetry
        "%venv_dir%\Scripts\pip.exe" install poetry-core
        "%venv_dir%\Scripts\pip.exe" install --force-reinstall %credentials_path%
        call "%venv_dir%\Scripts\activate.bat"
        poetry install
        call "%venv_dir%\Scripts\deactivate.bat"
        "%venv_dir%\Scripts\pip.exe" install --force-reinstall %mkdocs_insiders_path%
        echo =========================================
        echo Initialisierung abgeschlossen
        echo =========================================
    )
)
REM ==================================================
if "%arg_venv%"=="update" (
    "%venv_dir%\Scripts\python.exe" -m pip install --upgrade pip
    "%venv_dir%\Scripts\pip.exe" install --force-reinstall %credentials_path%
    call "%venv_dir%\Scripts\activate.bat"
    poetry install
    call "%venv_dir%\Scripts\deactivate.bat"
    REM "%venv_dir%\Scripts\pip.exe" install --force-reinstall %mkdocs_insiders_path%
)
REM ==================================================
cd /d "%script_dir%"
call "%venv_dir%\Scripts\activate.bat"
REM Pythonkommandos
call "%venv_dir%\Scripts\deactivate.bat"
endlocal
echo DONE
REM ==================================================