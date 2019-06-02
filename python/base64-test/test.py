#!/usr/bin/env python3

import base64

qwe='tro'
asd='lolo'

zxc =          base64.encodestring(bytes('{}{}'.format(qwe,asd),             'utf-8')).replace(b'\n', b'')
print(zxc)

username = "s.babik"
password = "n6SuswB9iybcKv1SGvPC"
base64string = base64.encodestring(bytes('{}:{}'.format(username, password), 'utf-8')).replace(b'\n', b'')
print(base64string)

