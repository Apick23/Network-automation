from netmiko import ConnectHandler
from pathlib import Path
from datetime import datetime
from getpass import getpass
def connect(devices: dict):
    with ConnectHandler(**devices) as conn:
        running_config = conn.send_command("show run")
    return running_config

password = getpass()

devices = {"host": "192.168.1.148",
           "username": "apickens",
           "password": password,
           "device_type": "cisco_ios"}

print(connect(devices))