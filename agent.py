## Code for the Agent that is running on the host system

from requests import post
from psutil import cpu_percent,virtual_memory,disk_usage
from json import dumps
from time import sleep

while True:

    cpu_percent = cpu_percent(interval=1)
    memory = virtual_memory()
    total_memory = memory.total / (1024 * 1024)
    disk_usage = disk_usage("/")

    payload_obj = {
        "cpu_percent":cpu_percent,
        "memory":total_memory,
        "disk_usage":disk_usage
    }

    payload = dumps(payload_obj)
    uri = "http://127.0.0.1:5050/update_metrics"
    response = post(url=uri,data=payload)
    sleep(15)