from codesys_opcua import CodesysOpcUa
from fluidsim_dde import FluidsimDdeClient
import time

fluidsim = FluidsimDdeClient()
fluidsim.connect()
plc_opcua = CodesysOpcUa(ip_plc='192.168.31.31', port=4840, fluidsim=fluidsim)

ctr = 0
while ctr < 100 or True:
    start_time = time.perf_counter()
    ctr += 1
    plc_opcua.update()
    fluidsim.update()
    # print(fluidsim.value_rx, fluidsim.value_tx)
    time.sleep(0.005)
    print(f'''{fluidsim.value_rx:03d} | {fluidsim.value_tx:03d} | {time.perf_counter():03.03f}s| {((time.perf_counter() - start_time)*1000.0):02.01f}ms''')

fluidsim.disconnect()
plc_opcua.disconnect()


























"""
https://gist.github.com/satishgunjal/b88af11483041ca538b4db4022c3360d
import subprocess
Erfassung WiFi SSID für die Konfiguration der IP Adresse Shelly
try:
    output = subprocess.check_output(['sudo', 'iwgetid']).decode()
    print("Connected Wifi SSID: " + output.split('"')[1])
except Exception, e:
    print e


=> Register Kommunikationsstatus in OPCUA Handler einfügen


Shelly AP-Mode
AP IP: 192.168.33.1

Konfiguration WiFi mit Priorisierung

network={
        ssid="hpna_fritz_box"
        psk="passwort"
        key_mgmt=WPA-PSK
        priority=1
}

network={
   ssid="ShellyPlus1PM-C82E18038098"
   key_mgmt=NONE
   priority=2
}


OFFENE PUNKTE
- Integration Shared Memory für aktives ein - ausschalten von Funktionen
- Integration System call
    - https://www.linkedin.com/pulse/run-linux-commands-from-codesys-jouke-aalvanger/
    - https://forge.codesys.com/forge/talk/Runtime/thread/dd10c05718/

"""
