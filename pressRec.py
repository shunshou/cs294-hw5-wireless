#!/usr/bin/env python
#Button press starts video for 5 seconds

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

CONSUMER_KEY = 'fSRyZAXOFg5dLhDyRSMd61bWJ'
CONSUMER_SECRET = '0iNvtlhTgIw1YEfXVbsMN5fj1WDF0hVd7EgV8jHfGoB7Oqx8cb'
ACCESS_KEY = '128685005-paZxFFlbEN5tCvW5Q8TTMmTffjJEYbNzpkOplwzz'
ACCESS_SECRET = 'Y3m46rkMo4ncp5BjWaEl8COVuboE619DdDWwrM76U3Ag1'





api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 



channel = 18
PROCNAME = "raspivid"

def runCam(channel):


   # piVid = subprocess.Popen(["time" "raspivid",  "-o",  "-", "-t"," 0", "-w", "640", "-h", "480", "-fps", "25", "-b", "2000000", "-g", "50"], stdout=subprocess.PIPE)
   # ffmpeg = subprocess.Popen(["/home/pi/arm/bin/ffmpeg", "-re", "-ar", "44100", "-ac", "2", "-acodec", "pcm_s16le", "-f", "s16le", "-ac", "2", "-i", "/dev/zero", "-f", "h264", "-i", "-", "-vcodec", "copy", "-acodec", "aac", "-ab", "128k", "-g", "50", "-strict", "experimental", "-f", "flv", "rtmp://a.rtmp.youtube.com/live2/shunshou.pyf1-dvt8-vdm5-8d02"], stdin=piVid.stdout)
   # print "runCam called"
    
    picam = subprocess.Popen(["raspistill", "-w",  "600", "-h"," 400", "-o", "/home/pi/piRestful/public/visitor.jpg", "-t", "1"], stdout=subprocess.PIPE)
    time.sleep(1);
    data = {"bell_rang" : "1"}
    req = urllib2.Request("http://morning-basin-3078.herokuapp.com")
    req.add_header("Content-Type","application/json")
    response = urllib2.urlopen(req, json.dumps(data))
    print response

    i = datetime.now()

    print i.strftime('%Y/%m/%d %H:%M:%S UTC')

    api.update_status(status='@cs294visitors You have a new visitor! '+i.strftime('%Y/%m/%d %H:%M:%S UTC'))


        
def camKill(channel):
    print "He's dead Jim"

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=3000)
GPIO.add_event_callback(channel, runCam)

#GPIO.wait_for_edge(17, GPIO.FALLING)
#piVid = subprocess.Popen(["raspivid",  "-o",  "-", "-t"," 0", "-w", "640", "-h", "480", "-fps", "25", "-b", "500000", "-g", "50"], stdout=subprocess.PIPE)
#subprocess.Popen([ ./ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/shunshou.b25p-r6vx-adac-8kc9"], shell=True)
#for line in piVid.stdout:
#    print line
#time.sleep(2)
#GPIO.wait_for_edge(17, GPIO.FALLING)
#for proc in psutil.process_iter():
#    if proc.name() == PROCNAME:
#         proc.kill()

while True:
    time.sleep(0.1)
