#!/usr/bin/env python2

from ruamel.yaml import YAML
import sys


schemaspyjson = """
stage: docs
image: $CI_REGISTRY/asdfgh/utility/schemaspy
services:
- name: gitlab.example:4567/asdfgh/utility/postgres
  alias: pg.tst
only:
- devel
allow_failure: true
before_script:
- eval $(ssh-agent -s)
- echo "$SSH_PRIVATE_KEY" | ssh-add -
- mkdir -p ~/.ssh
- ssh-keyscan -H de2np05d.dev.ves >> ~/.ssh/known_hosts
script:
- export_schema.sh
- |
  ssh skipper@de2np05d.dev.ves "mkdir -p /data/schemaspy/$CI_PROJECT_NAME  && \
                                sed -i '/label=\"paste\"/a \\          <a href=\"/$CI_PROJECT_NAME/\" class=\"list-group-item\">$CI_PROJECT_NAME</a>' /data/schemaspy/index.html"
- scp -r schemaspy/* skipper@de2np05d.dev.ves:/data/schemaspy/$CI_PROJECT_NAME/
"""


yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.preserve_quotes = True

#with open("test2.yml", 'r') as gitlab_file:
#    try:
#        schemaspyjson = yaml.load(gitlab_file)
#    except yaml.YAMLError as exc:
#        print(exc)



print(schemaspyjson)

#qq = yaml.load(schemaspyjson)

#yaml.dump(qq, sys.stdout)
yaml.dump(schemaspyjson, sys.stdout)
