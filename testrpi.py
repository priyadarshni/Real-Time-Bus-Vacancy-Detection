#!/usr/bin/env python


import os
import RPi.GPIO as gpio
import time
import datetime
import glob
#import MySQLdb
from time import strftime
import urllib

def connect_to_server():
	vacancy = 5
	url = 'http://192.168.1.104/write-to-database.py?temp='+str(vacancy)
        result = urllib.urlopen(url)

if __name__=="__main__":
  connect_to_server()

