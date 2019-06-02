#!/usr/bin/env python

import urllib2
import argparse
import ssl
import json
import base64

gitlab_token="1q2w3e4r"
context = ssl._create_unverified_context()

def get_tag_link(project):
    url = "https://mygitlab.com/nameOfGroup/{}/container_registry.json?private_token={}".format(project, gitlab_token)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, context=context)

    tags_json = json.loads(response.read())
    tags_array = {}
    for tag in tags_json:
        #print "{}".format(tag['tags_path'])
        tags_array[tag['path']] = tag['tags_path']
    return tags_array

print get_tag_link("admin_auth_mng")
