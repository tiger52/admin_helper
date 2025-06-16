#!/usr/bin/env python3

import jinja2
environment = jinja2.Environment()
template = environment.from_string('Domain - {{ domain | replace(".","-") }}')
print(template.render(domain="i.mycdn.com"))
