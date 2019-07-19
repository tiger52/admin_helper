#!/usr/bin/env python2

import argparse
import time
import urllib2
import ssl

context = ssl._create_unverified_context()

parser = argparse.ArgumentParser(description="Ping some http; OUTPUT is : time - url - response code - response time(miliseconds)")
parser.add_argument('--url', required=True, help='Define URL')
args = parser.parse_args()

# try to establish connection and check its status
starttime = time.time()
connection = urllib2.urlopen(args.url, context=context)
elapsed = time.time() - starttime
print("{} - {} - {} - {}ms".format(time.asctime(), args.url, connection.getcode(), elapsed))
