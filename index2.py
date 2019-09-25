#!/usr/bin/env python
# Server side code to read data sent by pi through GET method.

import cgi, cgitb
import os
import time
import datetime
import glob
import pymysql
from time import strftime
import urllib

# Create instance of FieldStorage 
form = cgi.FieldStorage() 
# Get data from client
vac = form.getvalue('vacancy') 

print( "Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Data Storage</title>")
print("</head>")
print("</html>" )

vacancy = float(vac)

# Alert user if recorded temperature is above a threshold (30 degrees in this case)

  
#Code to write the recorded temperature in the MYSQL database 'templog' and table 'temp-at-interrupt'
db = pymysql.connect(
    db='test',
    user='root',
    passwd='mysql',
    host='localhost')
cur = db.cursor()

  #dateWrite = time.strftime("%Y-%m-%d")
timeWrite = time.strftime("%H:%M:%S")
#sql = ""INSERT INTO rpitest (bus_id, vacancy,time) VALUES (1001,5,timeWrite)""

try:
	status=cur.execute("INSERT INTO rpitest (bus_id, vacancy,time) VALUES ('%d', '%d', '%s' )" % (1016,vacancy,timeWrite))
	status=db.commit()
  	print("\nProcess finished\n")
	cur.execute("SELECT * FROM rpitest")
	print([(r[0], r[1],r[2]) for r in cur.fetchall()])
except:
  	db.rollback()
  	print("\nProcess Failed to Complete")



cur.close()
db.close()



