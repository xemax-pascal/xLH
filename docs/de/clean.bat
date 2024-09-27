@echo off
setlocal
cls
echo "de\clean.bat"
:: ==================================================
cd /d %~dp0
set script_dir=%cd%
:: ==================================================
rd /s/q "docs"
rd /s/q "site"
rd /s/q "includes"
mkdir "docs"
mkdir "site"
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