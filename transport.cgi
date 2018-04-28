#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
import codecs
sys.path.append('/home/pi/git')
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)
print("Content-type: text/html; charset=UTF-8\n")

import cgi
form = cgi.FieldStorage()

print form.getvalue('weight'))
