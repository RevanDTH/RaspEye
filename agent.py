## Code for the Agent that is running on the host system

from requests import post
from psutil import cpu_percent,virtual_memory,disk_usage
from json import dumps
from time import sleep

while True:

    cpu_load = cpu_percent(interval=1)
    memory_info = virtual_memory()
    total_memory = memory_info.total / (1024 * 1024)
    disk_info = disk_usage("/")

    payload_obj = {
        "cpu_percent": cpu_load,
        "memory": total_memory,
        "disk_percent": disk_info.percent
    }

    payload = dumps(payload_obj)
    uri = "http://127.0.0.1:5050/api/update_metrics"
    response = post(url=uri, data=payload)
    print("Metrics sent . . .")
    sleep(15)