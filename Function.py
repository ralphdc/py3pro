#!/usr/bin/env python3

import requests
from config import Config

def send_request_json(method, url, data):

    headers = Config.HTTP_HEADER

    if method == 'get':
        res = requests.get(url=url, params=data, headers=headers)
    elif method == 'post':
        res = requests.post(url=url, data=data, headers=headers)
    else:
        raise Exception("[Error] - method error!")

    return res.json()



def send_request_text(method, url, data):

    headers = Config.HTTP_HEADER

    if method == 'get':
        res = requests.get(url=url, params=data, headers=headers)
    elif method == 'post':
        res = requests.post(url=url, data=data, headers=headers)
    else:
        raise Exception("[Error] - method error!")

    return res.text
