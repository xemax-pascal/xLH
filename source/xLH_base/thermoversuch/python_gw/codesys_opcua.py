import time
from shelly import Shelly
from opcua import Client, ua
import time


class CodesysOpcUa:
    def __init__(self, ip_plc='192.168.1.31', port=4840, shelly: Shelly = None):
        self.ip_plc = ip_plc
        self.port_plc = port
        self.shelly = shelly

        self._arData = [0.0 for i in range(12)]

        self._opcua_client = None
        self._arData_node = None
        self._bRelais_node = None
        self._sIpShelly_node = None

        self._node_root_base = None
        self._counter = 0.0
        self._start_time = time.perf_counter()

    def connect(self):
        self._opcua_client = Client(f'opc.tcp://{self.ip_plc}:{self.port_plc}')
        self._opcua_client.connect()
        root = self._opcua_client.get_root_node()
        plc_name = "4:CODESYS Control for Raspberry Pi 64 SL"
        node_root_base = ['0:Objects', '2:DeviceSet', plc_name,
                          '3:Resources', '4:app', '3:Programs', '4:io', '4:shelly']
        self._arData_node = root.get_child(node_root_base + ['4:arData'])
        self._bRelais_node = root.get_child(node_root_base + ['4:bRelais'])
        self._sIpShelly_node = root.get_child(node_root_base + ['4:sIpShelly'])

    def disconnect(self):
        self._opcua_client.disconnect()

    def reconnect(self):
        try:
            self.disconnect()
        except Exception as e:
            # print(e)
            # print('error disconnect')
            pass

        time.sleep(1.0)

        try:
            self.connect()
        except Exception as e:
            # print(e)
            # print('error reconnect')
            pass

    def read_write(self):
        try:
            if self._opcua_client is None:
                self.connect()

            self._arData[0] = float(self.shelly.bRelaisState)
            self._arData[1] = float(self.shelly.rVoltage)
            self._arData[2] = float(self.shelly.rCurrent)
            self._arData[3] = float(self.shelly.rPower)
            self._arData[4] = float(self.shelly.rTemperatureShelly)
            self._arData[5] = float(self.shelly.rTemperature1)
            self._arData[6] = float(self.shelly.rTemperature2)
            self._arData[7] = float(self.shelly.rTemperature3)
            self._arData[8] = float(self.shelly.iWifiRssi)

            perf_counter = time.perf_counter()
            cycle_time = perf_counter - self._start_time
            self._start_time = perf_counter
            self._counter += 0.1
            self._arData[9] = float(cycle_time * 1000.0)
            self._arData[10] = float(self._counter)
            self._start_time = time.perf_counter()

            self._arData_node.set_value(ua.Variant(self._arData, ua.VariantType.Float))
            self.shelly.bRelais = self._bRelais_node.get_value()
            self.shelly.ip_shelly = self._sIpShelly_node.get_value()

        except Exception as e:
            # print(e)
            # print('exception')
            self.reconnect()

    def update(self, print_cli=False):
        self.read_write()


if __name__ == '__main__':
    _shelly = Shelly(ip_shelly='')
    plc_opcua = CodesysOpcUa(ip_plc='192.168.1.31', port=4840, shelly=_shelly)

    ctr = 0
    while ctr < 5 or False:
        ctr += 1
        _shelly.update()
        plc_opcua.update()
        print(ctr, _shelly.bRelais, _shelly.bRelaisState)

    plc_opcua.disconnect()
