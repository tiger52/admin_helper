#!/usr/bin/env python

import ruamel.yaml
import sys

yyy1="""
trololo:
  qwe: 123
  asd: 456

megarow:
  zxc: 456
  yui: 789
"""
yaml1 = ruamel.yaml.YAML()
qqq1 = yaml1.load(yyy1)

print(qqq1["trololo"])

yyy2="""
fox:
  iop: 987
  lkj: 654
"""
yaml2 = ruamel.yaml.YAML()
qqq2 = yaml2.load(yyy2)

qqq1.update(qqq2)

yaml1.dump(qqq1, sys.stdout)

#with open('qqq.yaml', 'w') as outfile:
#    yamlspy.dump(qqq1, outfile)

