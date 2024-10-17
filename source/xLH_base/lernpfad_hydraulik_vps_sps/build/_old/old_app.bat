setlocal

cls
echo === build_exe.bat ===

set path_source=D:\Python\xLH_gw\source
set path_build=D:\Python\xLH_gw\build

set path_pyinstaller=D:\Python\xLH_gw\venv\Scripts\pyinstaller.exe
set path_packages=D:\Python\xLH_gw\venv\Lib\site-packages

rd /s/q "%path_build%\source"
robocopy "%path_source%" "source" /e

rd /s /q "xLH_gw"
rd /s /q "build"
rd /s /q "dist"

copy "app.spec" "source\app.spec"
copy "xemax.ico" "source\xemax.ico"
call D:\Python\xLH_gw\venv\Scripts\activate.bat
pyinstaller "source\app.spec"
REM %path_pyinstaller% "source\app.spec"


robocopy "dist\xLH_gw" "xLH_gw" /e
robocopy "%path_source%\data" "xLH_gw\data" /e

rd /s /q "build"
rd /s /q "dist"
rd /s /q "source"

endlocal
