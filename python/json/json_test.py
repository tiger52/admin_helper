#!/usr/bin/env python3
#import argpase
import json
#from urllib2 import urlopen

with open('example.json', 'r') as file:
    json_data = json.load(file)

json_data['qwe'] = '0.1'
print(json_data["qwe"])

