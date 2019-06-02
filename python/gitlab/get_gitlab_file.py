#!/usr/bin/python2

import sys
import ssl
import urllib2

context = ssl._create_unverified_context()

def rename_for_api(data):
    encoded = data
    encoded = encoded.replace('.', '%2E')
    encoded = encoded.replace('-', '%2D')
    encoded = encoded.replace('_', '%5F')
    encoded = encoded.replace('/', '%2F')
    return encoded

def get_project_file(data):
    gitlab_url = data['server_url']
    gitlab_token = data['request_token']
    project_id = data['project_id']
    path_in_project = rename_for_api(data['path_on_gitlab'])
    print(path_in_project)
    path_to_save = data['path']
    project_ref = data['project_ref']
    # https://mygitlab.com/api/v4/projects/1304/repository/files/priv%2Fdb%5Finit%2Esql/raw?ref=master
    url = "{}/api/v4/projects/{}/repository/files/{}/raw?ref={}".format(gitlab_url, project_id, path_in_project, project_ref)
    print(url)
    request = urllib2.Request(url)
    request.add_header('Private-Token', gitlab_token)
    response = urllib2.urlopen(request, context=context)
    filebody = response.read()
    with open(path_to_save, 'w') as f:
        f.write(filebody)


project = {
        "server_url": "https://mygitlab.com",
        "request_token": "KtERxDvHg_rn-d97z7Bk",
        "project_id": "1306",
        "path_on_gitlab": "priv/db_struct.sql",
        "path": "/home/tiger/python/gitlab/db_struct.sql",
        "project_ref": "master"
}

get_project_file(project)
	
