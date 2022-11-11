from nturl2path import url2pathname
from operator import methodcaller
from sqlite3 import Timestamp
from django.conf import settings
from django.db import connection
from django.template import Template, Context

import os
import psutil
import time
import json
import requests

class SimpleMiddleware(object):    
    def __init__(self, get_response):        
        self.get_response = get_response
    
    def __call__(self, request):

        start_time = time.time()

        response = self.get_response(request)

        timestamp = time.time()
        method = request.method
        url = request.path
        status_code = response.status_code
        latency = timestamp - start_time

        transaction_data = {
            'timestamp':int(timestamp),
            'method':method,
            'url':url,
            'status_code':status_code,
            'latency':latency
        }

        transaction_data = json.dumps(transaction_data)

        headers = {'Content-Type': 'application/json; charset=utf-8'}
        cookies = {'csrftoken': 'A0i3Fy1WbECkXis3LhOiDpyp0XMfLFXVUC0ECJivQe4UEoryvt4JdGsMy4eThkNd'}
        transaction_post = requests.post('http://127.0.0.1:8001/transaction/', data=transaction_data, headers=headers, cookies=cookies)

        return response