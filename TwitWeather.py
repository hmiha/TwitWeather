#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import twitter
from system import conf
import urllib
import urllib2
import json

# const
api = twitter.Api(
        consumer_key        = conf.consumer_key,
        consumer_secret     = conf.consumer_secret,
        access_token_key    = conf.access_token_key,
        access_token_secret = conf.access_token_secret,
        )

def tweet(desc):
    content = '@mhr380'
    content += '"""Tweeted by Bot"""'
    for item in desc:
        content += ' ' 
        content += item

    print content
    status = api.PostUpdate(content)
    #print 'tweet post result: \t%s' %status.text
    return

def get_weather():
    city = 'Ikoma,jp'
    url = 'http://api.openweathermap.org/data/2.5/forecast/daily?'
    query = {
            'q': 'Ikoma,jp',
            'mode': 'json',
            'units': 'metric',
            'cnt': '1',
            }
    req = urllib.urlencode(query)
    res = urllib2.urlopen(url + req)
    line = res.readline()
    #print line

    desc = []
    desc.append(city)

    weather = json.loads(line)['list'][0]['weather'][0]['description']
    desc.append(str(weather))

    desc.append('min:')
    temp_min = json.loads(line)['list'][0]['temp']['min']
    desc.append(str(temp_min))

    desc.append('max:')
    temp_max = json.loads(line)['list'][0]['temp']['max']
    desc.append(str(temp_max))

    return desc

if __name__ == '__main__':
    desc = get_weather()
    tweet(desc)
    time.sleep(86400)
