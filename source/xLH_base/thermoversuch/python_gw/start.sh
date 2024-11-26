# #!/bin/bash
# https://www.javatpoint.com/steps-to-write-and-execute-a-shell-script
# chmod +x start.sh
# execute: ./start.sh
# crontab -e
# @reboot sleep 20 && sudo bash /home/xlh/thermoversuch/start.sh
# python -m venv venv
# source venv/bin/activate
# deactivate
# python -m venv venv
# source venv/bin/activate

cd /home/xlh/thermoversuch
source venv/bin/activate
python thermoversuch.py
deactivate

