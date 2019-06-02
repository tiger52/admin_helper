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


def get_docker_tags(tag_link):
    url="https://mygitlab.com{}&per_page=1000&private_token={}".format(tag_link, gitlab_token)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, context=context)

    dockers_str= response.read()
    response_code = response.getcode()

    dockers_json = json.loads(dockers_str)

    dockers_json_sorted = sorted(dockers_json, key=lambda k: k['created_at'])

    for docker in dockers_json_sorted:
        print "{}\t{}\t{}".format(docker['name'], docker['created_at'], docker['revision'])
 
def get_docker_tags_list(tag_link):
    url="https://mygitlab.com{}&per_page=1000&private_token={}".format(tag_link, gitlab_token)
    req = urllib2.Request(url)
    response = urllib2.urlopen(req, context=context)

    dockers_str= response.read()
    response_code = response.getcode()

    dockers_json = json.loads(dockers_str)

    dockers_json_sorted = sorted(dockers_json, key=lambda k: k['created_at'])
    docker_tags_list = []

    for docker in dockers_json_sorted:
        docker_tags_list.append(docker['name'])

    return docker_tags_list

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

def get_id_from_repoID(project, docker_tag, repoID):
    url = "https://mygitlab.com:4567/v2/nameOfGroup/{}/manifests/{}".format(project, docker_tag)
    request = urllib2.Request(url)
    request.add_header("Accept", "application/vnd.docker.distribution.manifest.v2+json")
    registry_token = get_registry_token(project)
    request.add_header("Authorization", "Bearer {}".format(registry_token))

    response = urllib2.urlopen(request, context=context)
    response_headers = response.info()
    #print response_headers.dict['docker-content-digest']
    new_repoID = response_headers.dict['docker-content-digest']
    if repoID == new_repoID:
        return True
    else:
        return False

# === Main ===
parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--project', type=str, help='project in Vessel')
parser.add_argument('-s', '--sha', type=str, help='sha256 from kubernetes')
args = parser.parse_args()

if args.project is None:
	parser.print_help()
	exit()

#if args.sha is None:
#	parser.print_help()
#	exit()

for docker, link in get_tag_link(args.project).items():
    print "=== {} ===".format(docker)
    #get_docker_tags(link)
    if args.sha is None:
        get_docker_tags(link)
    else:
        for tag in  get_docker_tags_list(link):
            if get_id_from_repoID(args.project, tag, args.sha):
                print tag

