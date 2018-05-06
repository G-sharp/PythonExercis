#!/usr/bin/python
# -*- coding=utf8 -*-
import httplib
conn  = httplib.HTTPConnection("www.runoob.com")
conn.request("GET","/")
result = conn.getresponse()
contents = result.read()
print contents
