#!/usr/bin/env python
# -*- coding utf-8 -*-

from requests_oauthlib import OAuth1Session
import json

# Const
oauth_key_dict = {
    'consumer_key' : '6VflizqzpHBX6Lkxtod3p3ty3',
    'consumer_secret': '9NEwn8Cc2u44NnDLlWml8KIpLQmOHGNDl6GnG5T09M7XKY5EEB',
    'access_token': '448831066-mbYVsns6ycvUjH5Q3OvtdXe911yIru3f7lAr1HdV',
    'access_token_secret': 'TiDx1aIlsrN13zPX0PekjvJTgujh94QH4czhm54xF0ky6'
    }

# Func
def main():
    tweets = tweet_search('#python', oauth_key_dict)
    for tweet in tweets['statuses']:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']

        user_description = tweet[u'user'][u'screen_name']
        screen_name = tweet[u'user'][u'name']
        user_name = tweet[u'user'][u'name']

        print 'id:', tweet_id
        print 'text', text
        print 'created_at', created_at
        print 'user_id', user_id
        print 'user_desc', user_description
        print 'screen_name', screen_name
        print 'user_name', user_name
    return

def create_oauth_session(oauth_key_dict):
    oauth = OAuth1Session(
            oauth_key_dict['consumer_key'],
            oauth_key_dict['consumer_secret'],
            oauth_key_dict['access_token'],
            oauth_key_dict['access_token_secret']
            )

    return oauth

def tweet_search(search_word, oauth_key_dict):
    url = 'https://api.twitter.com/1.1/search/tweets.json?'
    params = {
            'q': unicode(search_word),
            'lang': 'ja',
            'result_type': 'recent',
            'count': '15'
            }
    oauth = create_oauth_session(oauth_key_dict)
    responce = oauth.get(url, params = params)
    if responce.status_code != 200:
        print 'error code: %d' %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

if __name__ == '__main__':
    main()


