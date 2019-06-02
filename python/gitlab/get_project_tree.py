#!/usr/bin/env python3

import requests
import argparse
import ssl
import json
import base64

gitlab_token="1q2w3e4r"
headers = {'Private-Token': gitlab_token}

#curl -s --request GET --header "Private-Token: KtERxDvHg_rn-d97z7Bk" 'https://mygitlab.com/api/v4/projects/?search=seed'

def get_project_id(project):
    url = "https://mygitlab.com/api/v4/projects/?search={}".format(project)
    response = requests.get(url, headers=headers)
    #print("{}\n{}\n\n{}\n\n{}\n\n".format(response.status_code, response.headers, response.text, response.json()))
    project_ids = response.json()
    project_id = None
    project_data_id = None
    for i in project_ids:
        if i['path'] == project:
            project_id = i['id']
            #print(project_id)
        if i['path'] == project + "_data":
            project_data_id = i['id']
    #print(type(project_id))
    return project_id, project_data_id
        
# https://mygitlab.com/api/v4/projects/1304/repository/tree?path=priv&ref=master
def get_project_tree(project_id, path_in_project, project_ref):
    url = "https://mygitlab.com/api/v4/projects/{}/repository/tree?path={}&ref={}&per_page=500".format(project_id, path_in_project, project_ref)
    response = requests.get(url, headers=headers)
    #print("{}\n{}\n\n{}\n\n{}\n\n".format(response.status_code, response.headers, response.text, response.json()))
    project_files_json = response.json()
    project_files = []
    for i in project_files_json:
        project_files.append(i['path'])
    return project_files

#project="admin_auth_mng"
#pr_id, pr_data_id = get_project_id(project)
#print(pr_id)
#print(get_project_tree(pr_id, "", "master"))

#for project in projects:
#    #print("{}: {}".format(project, get_project_id(project)))
#    pr_id, pr_data_id = get_project_id(project)

## === Main ===
parser = argparse.ArgumentParser(description="")
parser.add_argument('-p', '--project', type=str, help='project in registry')
parser.add_argument('-i', '--id', type=str, help='project ID in gitlab')
parser.add_argument('-t', '--tag', type=str, help='project reference')
parser.add_argument('-n', '--newtag', type=str, help='new docker tag')
args = parser.parse_args()

#if args.project is None:
#	parser.print_help()
#	exit()
if args.id is None:
	parser.print_help()
	exit()
if args.tag is None:
	parser.print_help()
	exit()
#if args.newtag is None:
#	parser.print_help()
#	exit()
#print(get_registry_token(args.project, 'push'))
#print(get_manifest(args.project, args.tag))
#change_tag(args.project, args.tag, args.newtag)
#print("name: {:20} project_id: {:5} project_data_id: {}".format(project, pr_id, pr_data_id))
listman = get_project_tree(args.id, "data/", args.tag)
for i in listman:
    print(i)
