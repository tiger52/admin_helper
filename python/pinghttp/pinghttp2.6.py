#!/usr/bin/env python2

import argparse
import time
import urllib2
import ssl
import sys

context = ssl._create_unverified_context()

parser = argparse.ArgumentParser(description="Ping some http; OUTPUT is : time - url - response code - response time(miliseconds)")
parser.add_argument('--url', required=True, help='Define URL')
parser.add_argument('--url2', help='Define seconds URL')
parser.add_argument('--sleep', default=2, help='seconds beetwen requests')
args = parser.parse_args()

def mypinghttp(url_to_ask):
    starttime = time.time()
    connection = urllib2.urlopen(url_to_ask, context=context)
    elapsed = time.time() - starttime
    print("{} - {} - {} - {}s".format(time.asctime(), args.url, connection.getcode(), elapsed))

def SIGINT():
	sys.stderr.write("\nBye-bye!\n")
	sys.exit(0)
	os.remove('onefile.txt')

try: 
    while True:
        mypinghttp(args.url)
        if args.url2 is not None:
            mypinghttp(args.url2)
        time.sleep(args.sleep)
except KeyboardInterrupt:
    SIGINT()	
