#!/usr/bin/env python3

import requests
import argparse
import ssl
import json
import base64

gitlab_token="1q2w3e4r"

def get_project_id(project):
    url = "https://mygitlab.com/api/v4/projects/?search={}".format(project)
    headers = {'Private-Token': gitlab_token}
    response = requests.get(url, headers=headers)
    #print("{}\n{}\n\n{}\n\n{}\n\n".format(response.status_code, response.headers, response.text, response.json()))
    project_ids = response.json()
    project_id = None
    project_data_id = None
    for i in project_ids:
        if i['path'] == project:
            project_id = i['id']
    return project_id
        
def get_project_jobs(project_id):
    url = "https://mygitlab.com/api/v4/projects/{}/jobs".format(project_id)
    headers = {'Private-Token': gitlab_token}
    response = requests.get(url, headers=headers)
    #print("{}\n{}\n\n{}\n\n{}\n\n".format(response.status_code, response.headers, response.text, response.json()))
    jobs_json = response.json()
    artifacts = []
    for job in jobs_json:
        print("{}".format(job['artifacts']))
 

#project="b2b"
#print(get_project_id("seed"))

#for project in projects:
#    #print("{}: {}".format(project, get_project_id(project)))
#    pr_id, pr_data_id = get_project_id(project)
#    print("name: {:20} project_id: {:5} project_data_id: {}".format(project, pr_id, pr_data_id))

#project_id="1306"
#get_project_branches(project_id)
project = 'weves'
get_project_jobs(get_project_id(project))



