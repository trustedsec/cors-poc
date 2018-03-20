#!/usr/bin/env python3
import cgi
import sys
import urllib.parse

# Read the POST request body submitted from corstest.html
postform = cgi.FieldStorage()
postdata = urllib.parse.unquote(postform['responsehtml'].value).replace('\\r\\n', '\r\n').replace('\\t', '\t')
sys.stderr.write(postdata)

# Write the POST data to disk
with open('captured-post-data.txt', 'a+') as outputfile:
    outputfile.writelines(postdata)
