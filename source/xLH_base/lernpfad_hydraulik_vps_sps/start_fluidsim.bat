@echo off
cls

set start_path=%cd%
echo start_path = %start_path%

cd /d "C:\Python\Fluidsim\fsp4\bin"
start fsp_stud.exe
cd /d "%start_path%"
