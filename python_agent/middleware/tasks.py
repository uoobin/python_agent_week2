from background_task import background

import os
import psutil
import time
import json
import requests

@background(schedule=0)
def get_usage():
    process = psutil.Process(os.getpid())

    cpu = process.cpu_percent()
    ram = process.memory_info().rss

    usage_data = {
    'cpu':cpu,
    'ram':ram
    }

    usage_data = json.dumps(usage_data)

    headers = {'Content-Type': 'application/json; charset=utf-8'}
    cookies = {'csrftoken': 'A0i3Fy1WbECkXis3LhOiDpyp0XMfLFXVUC0ECJivQe4UEoryvt4JdGsMy4eThkNd'}
    usage_post = requests.post('http://127.0.0.1:8001/usage/', data=usage_data, headers=headers, cookies=cookies)