#!/usr/bin/env python3

import requests
import argparse
import ssl
import json
import base64

#gitlab_token="1q2w3e4r"
gitlab_token="1q2w3e4r"
context = ssl._create_unverified_context()

def get_registry_token(project, action):
    url = "https://mygitlab.com/jwt/auth?client_id=docker&offline_token=true&service=container_registry&scope=repository:nameOfGroup/{}:{}".format(project, action)
    #url = "https://mygitlab.com/jwt/auth?client_id=docker&offline_token=true&service=mygitlab.com&scope=repository:nameOfGroup/{}:{}".format(project, action)
    username = "s.babik"
    password = "n6SuswB9iybcKv1SGvPC"

    base64string = base64.encodestring(bytes('{}:{}'.format(username, password), 'utf-8')).replace(b'\n', b'')
    headers = {'Authorization': "Basic {}".format(base64string.decode("utf-8"))}
    response = requests.get(url, headers=headers)
    print(response.status_code, response.headers, response.text)
    token_str = response.text
    token_json = json.loads(token_str)
    print(token_json)
    token = token_json['token']
    return token

def get_manifest(project, docker_tag):
    url = "https://mygitlab.com:4567/v2/nameOfGroup/{}/manifests/{}".format(project, docker_tag)
    registry_token = get_registry_token(project, 'pull')
    headers = {"Authorization": "Bearer {}".format(registry_token)}
    response = requests.get(url, headers=headers)
    return response.json()
    #return json.loads(response.text)

#    request = urllib2.Request(url)
#    #request.add_header("Accept", "application/vnd.docker.distribution.manifest.v2+json")
#    registry_token = get_registry_token(project)
#    request.add_header("Authorization", "Bearer {}".format(registry_token))
#
#    response = urllib2.urlopen(request, context=context)
#    response_headers = response.info()
#    #print response_headers.dict['docker-content-digest']
#    return json.loads(response.read())

def change_tag(project, old_tag, new_tag):
    url = "https://mygitlab.com:4567/v2/nameOfGroup/{}/manifests/{}".format(project, old_tag)
    #request.add_header("Accept", "application/vnd.docker.distribution.manifest.v2+json")
    registry_token = get_registry_token(project, 'push')
    headers = {"Authorization": "Bearer {}".format(registry_token)}

    body = get_manifest(project, old_tag)
    body['tag'] = new_tag
    response = requests.put(url, headers=headers, data=json.dumps(body))
    print("{}\n{}\n{}".format(response.status_code, response.headers, response.text))

#    response = urllib2.urlopen(request, context=context)
#    response_headers = response.info()
#    #print response_headers.dict['docker-content-digest']
#    print json.loads(response.read())


# === Main ===
parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--project', type=str, help='project in registry')
parser.add_argument('-t', '--tag', type=str, help='current docker tag')
parser.add_argument('-n', '--newtag', type=str, help='new docker tag')
args = parser.parse_args()

if args.project is None:
	parser.print_help()
	exit()
#if args.tag is None:
#	parser.print_help()
#	exit()
#if args.newtag is None:
#	parser.print_help()
#	exit()
print(get_registry_token(args.project, 'push'))
#print(get_manifest(args.project, args.tag))
#change_tag(args.project, args.tag, args.newtag)

