## Code for the Agent that is running on the host system

from requests import post
from psutil import cpu_percent,virtual_memory,disk_usage
from json import dumps
from time import sleep
from yaml import safe_load

with open("config.yaml") as f:
    config = safe_load(f)


while True:

    if config["agent"]["display_cpu"]: 
        cpu_load = cpu_percent(interval=1)
    else:
        cpu_load = None

    if config["agent"]["display_memory"]: 
        memory_info = virtual_memory()
        memory_percent = memory_info.percent
    else:
        memory_percent = None  
        
    if config["agent"]["display_disk"]: 
        disk_info = disk_usage("/").percent
    else:
        disk_info = None

    payload_obj = {
        "cpu_percent": cpu_load,
        "memory": memory_percent,
        "disk_percent": disk_info
    }

    payload = dumps(payload_obj)
    uri = config["agent"]["send_url"]
    response = post(url=uri, data=payload)
    sleep(15)