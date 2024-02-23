#!/usr/bin/python
import urllib.request

site = urllib.request.urlopen("http://businesscorp.com.br")
server = site.info()

print ("web server is running in: ")
print(server['SERVER'])
