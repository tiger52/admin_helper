#!/usr/bin/env python2.7

import argparse
import requests
import time

import urllib3
urllib3.disable_warnings()

parser = argparse.ArgumentParser(description="Ping some http; OUTPUT is : time - url - response code - response time(miliseconds)")
parser.add_argument('--url', required=True, help='Define URL')
args = parser.parse_args()

# try to establish connection and check its status
connection = requests.get(args.url, verify=False) 
print("{} - {} - {} - {}ms".format(time.asctime(), args.url, connection.status_code, connection.elapsed.microseconds/1000))
