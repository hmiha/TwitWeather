#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import *
import time

import twitter
from system import conf

# const
api = twitter.Api(
        consumer_key        = conf.consumer_key,
        consumer_secret     = conf.consumer_secret,
        access_token_key    = conf.access_token_key,
        access_token_secret = conf.access_token_secret,
        )

def tweet_test():
    timestamp = time.mktime(datetime.now().timetuple())
    status = api.PostUpdate(u'テスト timestamp = %s' % str(timestamp))
    print 'tweet post result: \t%s' %status.text
    return

def timeline_test():
    statuses = api.GetUserTimeline(
            screen_name = 'mhr380'
            )
    print '>>>timeline>>>'
    for s in statuses:
        print s.text.encode('utf8')

    return

if __name__ == '__main__':
    tweet_test()
    timeline_test()
