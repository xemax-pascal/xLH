import time
from fluidsim_dde import FluidsimDdeClient
from opcua import Client, ua
import time


class CodesysOpcUa:
    def __init__(self, ip_plc='192.168.31.31', port=4840, fluidsim: FluidsimDdeClient = None):
        self.ip_plc = ip_plc
        self.port_plc = port
        # self.user_plc = 'xlh'
        # self.password_plc = 'xlh'
        self.fluidsim = fluidsim

        self._opcua_client = None
        self._byIn_node = None
        self._byOut_node = None

        self._node_root_base = None


    def connect(self):
        self._opcua_client = Client(f'opc.tcp://{self.ip_plc}:{self.port_plc}')
        # self._opcua_client.set_user(self.user_plc)
        # self._opcua_client.set_password(self.password_plc)
        self._opcua_client.connect()
        root = self._opcua_client.get_root_node()
        plc_name = "4:CODESYS Control for Raspberry Pi 64 SL"
        node_root_base = ['0:Objects', '2:DeviceSet', plc_name,
                          '3:Resources', '4:app', '3:Programs']
        self._byIn_node = root.get_child(node_root_base + ["4:io_fs", '4:byFluidsimIn'])
        self._byOut_node = root.get_child(node_root_base + ["4:io_fs", '4:byFluidsimOut'])

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

            self.fluidsim.value_tx = self._byOut_node.get_value()
            self._byIn_node.set_value(ua.Variant(self.fluidsim.value_rx, ua.VariantType.Byte))

        except Exception as e:
            print(e)
            # print('exception')
            self.reconnect()

    def update(self, print_cli=False):
        self.read_write()


if __name__ == '__main__':
    _fluidsim = FluidsimDdeClient()
    plc_opcua = CodesysOpcUa(ip_plc='192.168.31.31', port=4840, fluidsim=_fluidsim)
    _fluidsim.connect()
    _fluidsim.update()
    plc_opcua.update()
    _fluidsim.update()
    print(_fluidsim.value_rx, _fluidsim.value_tx)

    plc_opcua.disconnect()
