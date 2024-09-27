@echo off
setlocal
cls
:: ==================================================
cd /d %~dp0
set script_dir=%cd%
cd ../..
set venv_dir=%cd%\venv
echo script_dir = %script_dir%
echo venv_dir = %venv_dir%
:: ==================================================
cd /d "%script_dir%"
:: echo %cd%
call "%venv_dir%\Scripts\activate"
mkdocs build
call "%venv_dir%\Scripts\deactivate"
:: ==================================================
cd /d "%script_dir%"
cd ..
robocopy "overrides\stylesheets" "de\site\stylesheets" /e /nfl /ndl /njh /njs /nc /ns /np
:: ==================================================
cd /d "%script_dir%"
robocopy "site" "site_de" /e /nfl /ndl /njh /njs /nc /ns /np
:: ==================================================
echo DONE
endlocal
:: ==================================================
:: https://ss64.com/nt/rd.html
:: https://ss64.com/nt/copy.html
:: https://ss64.com/nt/robocopy.html
:: https://adamtheautomator.com/robocopy/
:: https://build-system.fman.io/manual/
:: ==================================================
