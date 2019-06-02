#!/usr/bin/env python3

import requests
import argparse
import ssl
import json
import base64

gitlab_token="1q2w3e4r"

front_services=[
    "project1",
    "project2"
    ]


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
            #print(project_id)
        if i['path'] == project + "_data":
            project_data_id = i['id']
    #print(type(project_id))
    return project_id, project_data_id
        


#project="b2b"
#print(get_project_id("seed"))

for project in front_services:
    #print("{}: {}".format(project, get_project_id(project)))
    pr_id, pr_data_id = get_project_id(project)
    print("name: {:30} project_id: {:6} project_data_id: {}".format(project, pr_id, pr_data_id))
