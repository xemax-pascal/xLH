# from requests.auth import HTTPDigestAuth
from json.decoder import JSONDecodeError
import requests
from app_exceptions import *
from toolbox import check_ip_address


class Shelly:
    def __init__(self, ip_shelly):
        self.ip_shelly = ip_shelly

        self.bRelais = False
        self.bRelaisState = False
        self.rVoltage = 0.0
        self.rCurrent = 0.0
        self.rPower = 0.0
        self.rTemperatureShelly = 0.0
        self.rTemperature1 = 0.0
        self.rTemperature2 = 0.0
        self.rTemperature3 = 0.0
        self.iWifiRssi = 0

        self._status = None

    def read_status(self, raise_exception=False):
        if not check_ip_address(self.ip_shelly, raise_exception):
            return False

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'jsonrpc': '2.0',
                'id': 1,
                'method':
                    'Shelly.GetStatus',
                'params':
                    {'id': 0}
                }

        # credentials = HTTPDigestAuth('admin', '')
        credentials = None
        response = requests.post(f'http://{self.ip_shelly}/rpc',
                                 auth=credentials,
                                 headers=headers,
                                 json=data)

        # print(response.text)

        if response.status_code == 401:
            raise BadLogin()
        elif response.status_code == 404:
            raise NotFound("Not Found")

        try:
            response_data = response.json()
        except JSONDecodeError:
            raise BadResponse("Bad JSON")

        if "error" in response_data:
            error_code = response_data["error"].get("code", None)
            error_message = response_data["error"].get("message", "")

            if error_code == 401:
                raise BadLogin(error_message)
            elif error_code == 404:
                raise NotFound(error_message)
            else:
                raise BadResponse("{}: {}".format(error_code, error_message))

        if response_data["id"] != 1:
            raise BadResponse("invalid payload id was returned")

        self._status = response.json()
        self.values()

        return True

    def write_relais(self, raise_exception=False):
        if not check_ip_address(self.ip_shelly, raise_exception):
            return False

        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'jsonrpc': '2.0',
                'id': 1,
                'method':
                    'Switch.Set',
                'params':
                    {'id': 0,
                     'on': self.bRelais}
                }
        # credentials = HTTPDigestAuth('admin', '')
        credentials = None

        response = requests.post(f'http://{self.ip_shelly}/rpc',
                                 auth=credentials,
                                 headers=headers,
                                 json=data,
                                 timeout=4)

        if response.status_code == 401:
            raise BadLogin()
        elif response.status_code == 404:
            raise NotFound("Not Found")

        try:
            response_data = response.json()
        except JSONDecodeError:
            raise BadResponse("Bad JSON")

        if "error" in response_data:
            error_code = response_data["error"].get("code", None)
            error_message = response_data["error"].get("message", "")

            if error_code == 401:
                raise BadLogin(error_message)
            elif error_code == 404:
                raise NotFound(error_message)
            else:
                raise BadResponse("{}: {}".format(error_code, error_message))

        if response_data["id"] != 1:
            raise BadResponse("invalid payload id was returned")

        return True

    def values(self):
        self.bRelaisState = self._status['result']['switch:0']['output']
        self.rVoltage = self._status['result']['switch:0']['voltage']
        self.rCurrent = self._status['result']['switch:0']['current']
        self.rPower = self._status['result']['switch:0']['apower']
        self.rTemperatureShelly = self._status['result']['switch:0']['temperature']['tC']
        self.rTemperature1 = self._status['result']['temperature:100']['tC']
        self.rTemperature2 = self._status['result']['temperature:101']['tC']
        self.rTemperature3 = self._status['result']['temperature:102']['tC']

        self.iWifiRssi = self._status['result']['wifi']['rssi']

    def reset(self):
        self.bRelais = False
        self.bRelaisState = False
        self.rVoltage = 0.0
        self.rCurrent = 0.0
        self.rPower = 0.0
        self.rTemperatureShelly = 0.0
        self.rTemperature1 = 0.0
        self.rTemperature2 = 0.0
        self.rTemperature3 = 0.0
        self.iWifiRssi = 0

    def __str__(self):
        str_out = f'Shelly {self.ip_shelly = }\n'

        str_out += f'{self.bRelais = }\n'
        str_out += f'{self.bRelaisState = }\n'

        str_out += f'{self.rVoltage = } V\n'
        str_out += f'{self.rCurrent = } A\n'
        str_out += f'{self.rPower = } W\n'
        # str_out += f'{self.arEnergyMinute = } ?\n'
        # str_out += f'{self.rEnergyMinuteTs = } ?\n'

        str_out += f'{self.rTemperatureShelly = } °C\n'
        str_out += f'{self.rTemperature1 = } °C\n'
        str_out += f'{self.rTemperature2 = } °C\n'
        str_out += f'{self.rTemperature3 = } °C\n'

        str_out += f'{self.iWifiRssi = }'
        return str_out

    def update(self, print_cli=False):
        try:
            self.read_status(raise_exception=True)
        except Exception as e:
            self.reset()
            if print_cli:
                print(e)
                print('error shelly')

        if self.bRelais != self.bRelaisState:
            try:
                self.write_relais(raise_exception=True)
            except Exception as e:
                if print_cli:
                    print(e)
                    print('error shelly')


if __name__ == '__main__':
    # shelly = Shelly(ip_shelly='192.168.1.41')
    shelly = Shelly(ip_shelly='172.16.23.29')
    shelly.read_status(raise_exception=True)
    # shelly.bRelais = True
    # shelly.update(print_cli=True)
    print(shelly)


"""
AP IP: 192.168.33.1
    Konfiguration: sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    network={
       ssid="ShellyPlus1PM-C82E18038098"
       key_mgmt=NONE
    }
"""