#!/usr/bin/env python
#import argpase
import json
from urllib2 import urlopen

j = urlopen('http://k21-rec.prod.oll.tv:8080/api/v1/status/')
json_data = json.load(j)

print "running:{} waiting_count:{}".format(json_data["running"],json_data["waiting_count"])

