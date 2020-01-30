#!/usr/bin/env python

#from ruamel.yaml import yaml
import ruamel.yaml
#import yaml

yaml = ruamel.yaml.YAML()
with open("gitlab-ci.yaml", 'r') as gitlab_file:
    try:
        gitlab_ci = yaml.load(gitlab_file)
        print gitlab_ci
    except yaml.YAMLError as exc:
        print(exc)

# change view of Deploy script
if 'variables' in gitlab_ci:
    tag = "DEPLOY_SCRIPT"
    if tag in gitlab_ci['variables']:
        deploy_script = ruamel.yaml.scalarstring.LiteralScalarString(u"sh -c 'hostname &&\nmkdir -p ~/app &&\ncd ~/app &&\ngit clone -b $CI_COMMIT_REF_NAME git@gitlab.example:asdfgh/$CI_PROJECT_NAME.git ;\ncd $CI_PROJECT_NAME &&\ngit checkout $CI_COMMIT_REF_NAME &&\ngit pull &&\nrm -rf _build/ ;\nrebar3 as $CI_COMMIT_REF_NAME release &&\n_build/$CI_COMMIT_REF_NAME/rel/$CI_PROJECT_NAME/bin/$CI_PROJECT_NAME stop ;\n_build/$CI_COMMIT_REF_NAME/rel/$CI_PROJECT_NAME/bin/$CI_PROJECT_NAME start'\n")

        del gitlab_ci['variables'][tag]
        gitlab_ci['variables'][tag] = deploy_script

        if 'deploy devel' in gitlab_ci:
            for i in gitlab_ci['deploy devel']['script']:
                i_index = gitlab_ci['deploy devel']['script'].index(i)
                gitlab_ci['deploy devel']['script'][i_index] = gitlab_ci['deploy devel']['script'][i_index].replace(' $DEPLOY_SCRIPT', ' \"$DEPLOY_SCRIPT\"')

# set corect oreder in stages
j=0
for i in gitlab_ci['build docker']['services'][0]['command']:
    gitlab_ci['build docker']['services'][0]['command'][j] = '\"{}\"'.format(i)
    j += 1

#stages
if gitlab_ci['stages'].index('release') < gitlab_ci['stages'].index('deploy'):
    i1 = gitlab_ci['stages'].index('release')
    i2 = gitlab_ci['stages'].index('deploy')
    gitlab_ci['stages'][i1] = 'deploy'
    gitlab_ci['stages'][i2] = 'release'

# edit docs
print gitlab_ci['all docs']
if 'cover report' in gitlab_ci:
    if 'only' in gitlab_ci['cover report']:
        if 'tags' in gitlab_ci['cover report']['only']:
            gitlab_ci['cover report']['only'].remove('tags')
        if 'master' in gitlab_ci['cover report']['only']:
            gitlab_ci['cover report']['only'].remove('master')
        if 'rc' in gitlab_ci['cover report']['only']:
            gitlab_ci['cover report']['only'].remove('rc')
    else:
        gitlab_ci['cover report'].update({'only': []})
        gitlab_ci['cover report']['only'].append('devel')
 
if 'all docs' in gitlab_ci:
    if 'only' in gitlab_ci['all docs']:
        if 'tags' in gitlab_ci['all docs']['only']:
            gitlab_ci['all docs']['only'].remove('tags')
        if 'master' in gitlab_ci['all docs']['only']:
            gitlab_ci['all docs']['only'].remove('master')
        if 'rc' in gitlab_ci['all docs']['only']:
            gitlab_ci['all docs']['only'].remove('rc')
    else:
        gitlab_ci['all docs'].update({'only': []})
        gitlab_ci['all docs']['only'].append('devel')

if 'swagger' in gitlab_ci:
    if 'only' in gitlab_ci['swagger']:
        if 'tags' in gitlab_ci['swagger']['only']:
            gitlab_ci['swagger']['only'].remove('tags')
        if 'master' in gitlab_ci['swagger']['only']:
            gitlab_ci['swagger']['only'].remove('master')
        if 'rc' in gitlab_ci['swagger']['only']:
            gitlab_ci['swagger']['only'].remove('rc')
    else:
        gitlab_ci['swagger'].update({'only': []})
        gitlab_ci['swagger']['only'].append('devel')

# edit build docker
tag="devel"
if tag in gitlab_ci['build docker']['only']:
    gitlab_ci['build docker']['only'].remove(tag)

tag="stage"
if tag in gitlab_ci['build docker']['only']:
    gitlab_ci['build docker']['only'].remove(tag)

tag="master"
if tag not in gitlab_ci['build docker']['only']:
    gitlab_ci['build docker']['only'].append(tag)

# edit deploy to k8s
tag="devel"
if tag in gitlab_ci['.deploy to k8s']['only']:
    gitlab_ci['.deploy to k8s']['only'].remove(tag)

tag="stage"
if tag in gitlab_ci['.deploy to k8s']['only']:
    gitlab_ci['.deploy to k8s']['only'].remove(tag)

tag="master"
if tag not in gitlab_ci['.deploy to k8s']['only']:
    gitlab_ci['.deploy to k8s']['only'].append(tag)

tag = "stage"
if tag in gitlab_ci['.deploy to k8s']:
    del gitlab_ci['.deploy to k8s'][tag]



with open('data.yaml', 'w') as outfile:
    #yaml.dump(gitlab_ci, outfile, default_flow_style=True, allow_unicode=True)
    yaml.dump(gitlab_ci, outfile)





