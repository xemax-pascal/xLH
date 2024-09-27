@echo off
setlocal
cls
:: ==================================================
cd /d %~dp0
set script_dir=%cd%
set venv_dir=%cd%\venv
echo script_dir = %script_dir%
echo venv_dir = %venv_dir%
:: ==================================================
cd /d "%venv_dir%"
"%venv_dir%\Scripts\python.exe" -m pip install --upgrade pip
call "%venv_dir%\Scripts\activate"

python -m pip install --upgrade pip
pip install --upgrade setuptools
REM pip install -r "%script_dir%\requirements.txt"
REM pip install --force-reinstall "D:\Python\mkdocs-material-insiders"

call "%venv_dir%\Scripts\deactivate"
:: ==================================================
:: ==================================================
echo DONE
endlocal
:: ==================================================
