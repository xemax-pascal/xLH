REM https://medium.com/@informationsecurity/remote-ssh-tunneling-with-plink-exe-7831072b3d7d
REM sudo apt-get install bmon
REM https://www.tecmint.com/bmon-network-bandwidth-monitoring-debugging-linux/

set ip_pi=192.168.31.31
set port=62555
set user=xlh
set pw=xlh

plink -ssh -l %user% -pw %pw% -R %ip_pi%:%port%:127.0.0.1:%port% %ip_pi% -t bmon -p usb0
