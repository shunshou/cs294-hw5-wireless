#!/usr/bin/env python
import sys

from datetime import datetime

from twython import Twython

CONSUMER_KEY = 'fSRyZAXOFg5dLhDyRSMd61bWJ'
CONSUMER_SECRET = '0iNvtlhTgIw1YEfXVbsMN5fj1WDF0hVd7EgV8jHfGoB7Oqx8cb'
ACCESS_KEY = '128685005-paZxFFlbEN5tCvW5Q8TTMmTffjJEYbNzpkOplwzz'
ACCESS_SECRET = 'Y3m46rkMo4ncp5BjWaEl8COVuboE619DdDWwrM76U3Ag1'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 

i = datetime.now()

print i.strftime('%Y/%m/%d %H:%M:%S UTC')

api.update_status(status='@cs294visitors You have a new visitor! '+i.strftime('%Y/%m/%d %H:%M:%S UTC'))
