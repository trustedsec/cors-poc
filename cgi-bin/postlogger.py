#!/usr/bin/env python3
import cgi
import sys
import urllib.parse

postform = cgi.FieldStorage()
postdata = urllib.parse.unquote(postform['responsehtml'].value).replace('\\r\\n', '\r\n').replace('\\t', '\t')
sys.stderr.write(postdata)
with open('captured-post-data.txt', 'a+') as outputfile:
    outputfile.writelines(postdata)
