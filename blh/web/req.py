#!/usr/bin/python
import urllib2

url = "http://www.google.com"

headers = {}
headers['User-Agent'] = "Googlebot"

req = urllib2.Request(url, headers=headers)
res = urllib2.urlopen(req)

print res.read()
res.close()
