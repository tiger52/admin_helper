#!/usr/bin/env python
import sys
import cgi
import cgitb
cgitb.enable()

sys.stderr = sys.stdout
print "Content-Type: text/html\n"

print "<title>test cgi</title>"
print "<h1>test cgi</h1>"
print "<input type='form' name=app value='123'>"


form = cgi.FieldStorage()

cgi.print_form(form)

