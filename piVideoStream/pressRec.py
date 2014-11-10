#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
import psutil
import os
import urllib2
import json
import sys

from datetime import datetime
from twython import Twython

# Twitter bot setup
# See http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

# Button on GPIO 18
channel = 18

# Action when button pressed
def runCam(channel):
    
    # Quickly take photo 
    picam = subprocess.Popen(["raspistill", "-w",  "600", "-h"," 400", "-o", "/home/pi/piRestful/public/visitor.jpg", "-t", "1"], stdout=subprocess.PIPE)

    # Wait so that bell_rang POST notification is sent AFTER the visitor image has been updated
    time.sleep(1);
    data = {"bell_rang" : "1"}
    req = urllib2.Request("http://morning-basin-3078.herokuapp.com")
    req.add_header("Content-Type","application/json")
    response = urllib2.urlopen(req, json.dumps(data))
    print response

    # Send current time and Web app location to Twitter
    i = datetime.now()
    print i.strftime('%Y/%m/%d %H:%M:%S UTC \r\n')
    api.update_status(status='@cs294visitors You have a new visitor! http://morning-basin-3078.herokuapp.com  '+i.strftime('%Y/%m/%d %H:%M:%S UTC'))

# Setup button GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=3000)
GPIO.add_event_callback(channel, runCam)

while True:
    time.sleep(0.1)
