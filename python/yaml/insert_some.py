#!/usr/bin/env python

#from collections import OrderedDict
from ruamel.yaml import YAML
import sys

d = """
a:
  r: 5
  t: 6
c:
  y: 7
  u: 8
b: 2
f: 4
"""

f = """
g: "qwerty qwerty qwerty qwerty qwerty qwerty qwerty qwerty
    qwerty qwerty qwerty qwerty qwerty qwerty qwerty qwerty "
h: 4
"""

def insert_after(d1, d2, key):
    i = 0
    if key in d1:
        for d1_key in d1.keys():
            i += 1
            if d1_key == key: break
    d1.insert(i, "test", d2, )
    return d1
    #YAML().dump(d1, sys.stdout)

def insert_before(d1, d2, key):
    i = 0
    if key in d1:
        for d1_key in d1.keys():
            i += 1
            if d1_key == key: break
    d1.insert(i-1, "test", d2, )
    return d1
    #YAML().dump(d1, sys.stdout)



yaml = YAML()
yaml.indent = 2
yaml.width = 4096
q1 = yaml.load(d)
q2 = yaml.load(f)

#print(q1.iter('a'))

#q1.insert(1, "test", q2, )
#yaml.dump(q1, sys.stdout)

#with open('test.yml', 'w') as outfile:
#    yaml.dump(qq, outfile)
#yaml.dump(qq, sys.stdout)
#yaml.dump(q1, sys.stdout)

w1 = insert_after(q1, q2, "b")
yaml.dump(w1, sys.stdout)
print("====")
w2 = insert_after(w1, q2, "b")
yaml.dump(w2, sys.stdout)

#for i in q1.iteritems():
#    print(i)
