#!/usr/bin/env python3

import requests

url = 'https://google.com'
rrr = requests.get(url)
print(rrr.status_code)
print(rrr.text())
