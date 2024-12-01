import tomli
import sys, os, pathlib

def get_app_path():
    if getattr(sys, 'frozen', False):
        # If the application is run as a bundle, the PyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        # app_path = sys._MEIPASS
        app_path = str(pathlib.Path(sys._MEIPASS).parents[0].as_posix())
    else:
        app_path = str(pathlib.Path(__file__).parents[0].as_posix())
    return app_path


def read_toml_config():
    # https://toml.io/en/
    with open(f'''{get_app_path()}/config.txt''', "rb") as f:
        toml_dict = tomli.load(f)
    return toml_dict

class Config:
    def __init__(self):
        self.plc_ip = None
        self.plc_user = None
        self.plc_password = None
        self.webvisu_port = None
        self.opcua_port = None
        self.opcua_user = None
        self.opcua_password = None
        self.opcua_plc_name = None
        self.fluidsim_dde_server = None
        self.fluidsim_dde_topic = None
        self.fluidsim_dde_item_rx = None
        self.fluidsim_dde_item_tx = None
        self.set_config()

    def set_config(self):
        data_dict = read_toml_config()
        self.plc_ip = data_dict['plc']['ip']
        # self.plc_user = data_dict['plc']['user']
        # self.plc_password = data_dict['plc']['password']
        self.webvisu_port = data_dict['plc']['webvisu_port']
        self.opcua_port = data_dict['opcua']['port']
        # self.opcua_user = data_dict['opcua']['user']
        # self.opcua_password = data_dict['opcua']['password']
        self.opcua_plc_name = data_dict['opcua']['plc_name']
        self.fluidsim_dde_server = data_dict['fluidsim_dde']['server']
        self.fluidsim_dde_topic = data_dict['fluidsim_dde']['topic']
        self.fluidsim_dde_item_rx = data_dict['fluidsim_dde']['item_rx']
        self.fluidsim_dde_item_tx = data_dict['fluidsim_dde']['item_tx']

    def __str__(self):
        return str(self.__dict__)


if __name__ == "__main__":
    print(get_app_path())
    print(read_toml_config())
    _config = Config()
    print(_config)

# https://pypi.org/project/tomli/