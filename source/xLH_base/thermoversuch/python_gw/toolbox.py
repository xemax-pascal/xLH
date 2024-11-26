from app_exceptions import IpNotValid
import ipaddress


def check_ip_address(ip_address, raise_exception=False):
    try:
        ipaddress.ip_address(ip_address)
        return True
    except Exception as e:
        # print('ip_shelly is invalid')
        if raise_exception:
            raise IpNotValid(f'IP not valid {ip_address}')
        return False
