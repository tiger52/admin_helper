#!/usr/bin/env python

import urllib2
import argparse
import ssl
import json
import base64

gitlab_token="1q2w3e4r"
context = ssl._create_unverified_context()

def get_registry_token(project):
    url = "https://mygitlab.com/jwt/auth?client_id=docker&offline_token=true&service=container_registry&scope=repository:nameOfGroup/{}:pull".format(project)
    username = "s.babik"
    password = "n6SuswB9iybcKv1SGvPC"

    base64string = base64.encodestring('{}:{}'.format(username, password)).replace('\n', '')
    request = urllib2.Request(url)
    request.add_header("Authorization", "Basic {}".format(base64string))
    response = urllib2.urlopen(request, context=context)
    token_str = response.read()
    token_json = json.loads(token_str)
    token = token_json['token']
    return token

def get_manifest(project, docker_tag):
    url = "https://mygitlab.com:4567/v2/nameOfGroup/{}/manifests/{}".format(project, docker_tag)
    request = urllib2.Request(url)
    #request.add_header("Accept", "application/vnd.docker.distribution.manifest.v2+json")
    registry_token = get_registry_token(project)
    request.add_header("Authorization", "Bearer {}".format(registry_token))

    response = urllib2.urlopen(request, context=context)
    response_headers = response.info()
    #print response_headers.dict['docker-content-digest']
    return json.loads(response.read())

def change_tag(project, old_tag, new_tag):
    url = "https://mygitlab.com:4567/v2/nameOfGroup/{}/manifests/{}".format(project, old_tag)
    request = urllib2.Request(url)
    #request.add_header("Accept", "application/vnd.docker.distribution.manifest.v2+json")
    registry_token = get_registry_token(project)
    request.add_header("Authorization", "Bearer {}".format(registry_token))

    body = get_manifest(project, old_tag)
    body['tag'] = '0.1'

    request.add_data(body)
#    response = urllib2.urlopen(request, context=context)
#    response_headers = response.info()
#    #print response_headers.dict['docker-content-digest']
#    print json.loads(response.read())


# === Main ===
parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--project', type=str, help='project in registry')
parser.add_argument('-t', '--tag', type=str, help='docker tag')
args = parser.parse_args()

if args.project is None:
	parser.print_help()
	exit()

change_tag(args.project, args.tag, '0.1')

#get_manifest(args.project, args.tag)

