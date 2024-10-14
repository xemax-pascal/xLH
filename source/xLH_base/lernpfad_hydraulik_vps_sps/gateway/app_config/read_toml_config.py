import tomli
from app_config.get_app_path import get_app_path

def read_toml_config():
    with open(f'''{get_app_path()}/config.toml''', "rb") as f:
        toml_dict = tomli.load(f)
    return toml_dict

if __name__ == "__main__":
    print(read_toml_config())

# https://pypi.org/project/tomli/