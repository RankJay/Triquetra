import requests
from time import time

import os

def retweetersScraping(TWEET_ID):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print('running from', dir_path)

    tweet_id = TWEET_ID
    key = '56iEG9xVd1ToyEoAWJN9PxW1j'
    secret = 'E84NQiMXKBXa7oFAHzL3aFfXY8Yr061UGJRVvXAWDMjfAXCQ40'
    ts = int(time())

    auth_url = "https://api.twitter.com/oauth2/token"
    data = {'grant_type': 'client_credentials'}
    auth_resp = requests.post(auth_url, auth=(key, secret), data=data)
    token = auth_resp.json()['access_token']


    url = 'https://api.twitter.com/1.1/statuses/retweets/%s.json?count=100' % tweet_id
    headers = {'Authorization': 'Bearer %s' % token}
    retweets_resp = requests.get(url, headers=headers)

    retweets = retweets_resp.json()

    retweeters = [(r['user']['screen_name'], r['user']['id']) for r in retweets]

    with open('retweeters-ids-%s.txt' % (tweet_id), 'w') as f_out:
        for r, i in retweeters:
            f_out.write('%s,%s\n' % (r, i))

    print('done')