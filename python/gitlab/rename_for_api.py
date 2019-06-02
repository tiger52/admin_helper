#!/usr/bin/env python3

import sys
import urllib.parse

encoded = urllib.parse.quote(sys.argv[1])
encoded = encoded.replace('.', '%2E')
encoded = encoded.replace('-', '%2D')
encoded = encoded.replace('_', '%5F')
encoded = encoded.replace('/', '%2F')

print(encoded)

