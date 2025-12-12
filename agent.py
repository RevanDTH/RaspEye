## Code for the Agent that is running on the host system

import requests
import psutil
import json

cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
total_memory = memory.total / (1024 * 1024)
disk_usage = psutil.disk_usage("/")

payload_obj = {
    "cpu_percent":cpu_percent,
    "memory":total_memory,
    "disk_usage":disk_usage
}

payload = json.dumps(payload_obj)


uri = "http://127.0.0.1:5050/update_metrics"

response = requests.post(url=uri,data=payload)