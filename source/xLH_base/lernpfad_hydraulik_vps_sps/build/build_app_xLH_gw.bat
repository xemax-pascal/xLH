REM ==================================================
echo === app.bat ===
@echo off
setlocal
cls
REM ==================================================
cd /d %~dp0
set script_path=%cd%
set xlh_gw_path=%cd%\xLH_gw
cd ..
set source_path=%cd%\gateway
REM cd ..\..\..
REM set venv_path=%cd%\venv
set venv_path=D:\Python\xLH_gw\venv
echo script_path = %script_path%
echo xlh_gw_path = %xlh_gw_path%
echo source_path = %source_path%
echo venv_path = %venv_path%
REM ==================================================
cd /d "%script_path%"
rd /s /q "source"
rd /s /q "xLH_gw"
rd /s /q "build"
rd /s /q "dist"
robocopy "%source_path%" "source" /e
copy "app.spec" "source\app.spec"
copy "xemax.ico" "source\xemax.ico"
REM ==================================================
call "%venv_path%\Scripts\activate.bat"
pyinstaller "source\app.spec"
robocopy "dist\xLH_gw" "xLH_gw" /e
REM robocopy "%path_source%\data" "xLH_gw\data" /e
copy "%source_path%\config\config.txt" "%xlh_gw_path%\config.txt"
REM ==================================================
rd /s /q "source"
rd /s /q "build"
rd /s /q "dist"
REM ==================================================
endlocal
