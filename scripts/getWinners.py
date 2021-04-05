from glob import glob
from random import shuffle

import requests

coupon_codes = [
    'mlbookcamp-1',
    'mlbookcamp-2',
    'mlbookcamp-3',
    'mlbookcamp-4',
    'mlbookcamp-5',
    'mlbookcamp-6',
    'mlbookcamp-7',
    'mlbookcamp-8',
]

top = 10 # len(coupon_codes)

def returnLimit():
    return top

def randomGiveaway(TWEET_ID, OWNER_NAME):
    tweet_id = TWEET_ID
    handle = OWNER_NAME

    key = '56iEG9xVd1ToyEoAWJN9PxW1j'
    secret = 'E84NQiMXKBXa7oFAHzL3aFfXY8Yr061UGJRVvXAWDMjfAXCQ40'

    auth_url = "https://api.twitter.com/oauth2/token"
    data = {'grant_type': 'client_credentials'}
    auth_resp = requests.post(auth_url, auth=(key, secret), data=data)
    token = auth_resp.json()['access_token']

    headers = {'Authorization': 'Bearer %s' % token}

    # get followers

    all_followers = set()

    next_cursor = -1

    while next_cursor != 0:
        followers_url = 'https://api.twitter.com/1.1/followers/ids.json?cursor=%s&' + \
                    'screen_name=%s&count=5000'
        followers_url = followers_url % (next_cursor, handle)

        followers_resp = requests.get(followers_url, headers=headers).json()
        followers_list = followers_resp['ids']

        all_followers.update(followers_list)
        print('num_followers', len(all_followers))
        
        next_cursor = followers_resp['next_cursor']
        print('next_cursor =', next_cursor)


    # get retweeters
    
    retweeter_files = sorted(glob('retweeters-ids-%s.txt' % tweet_id)) 
    all_retweeters = {}

    with open('retweeters-ids-%s.txt' % tweet_id, 'r') as f_in: 
        for line in f_in:
            screen_name, user_id = line.strip().split(',')
            user_id = int(user_id)
            all_retweeters[user_id] = screen_name

        print('num_retweeters', len(all_retweeters))


    # selecting winners
    valid = list(all_retweeters.values())
    shuffle(valid)

    ids = list(all_retweeters.keys())
    # winners_ids = valid[:top]
    # winners = [all_retweeters[i] for i in winners_ids]

    # print('winners:')
    # for i in winners:
    #     print('@%s' % i)

        
    template = """
    Hi @{name},\nThank you for participating in the giveaway of ChainLink.\nHere's the uniswap address of the ETH-GPR Pool that you will use to avail your GPR tokens: 0x031e848a47e45d716aa8abedfa715307c8b9dda2.\nTo get it\n1) Make your metamask wallet\n2) Go to Uniswap. https://app.uniswap.org/#/swap\n3) Connect your Metamask wallet\n4) Set to Goerli Testnet in your Metamask Wallet\n5) Send your Metamask Wallet address in this chat like this (#EthAddress):\ne.g. #0x4CAdaFc96CdB5d86c96aD92a872767FB525C8027\nI hope you find it useful!\nPlease get in touch if you have any questions.\n\nFrom,\nCleopatra.
    """.strip()

    # print('messages:')


    # for n in winners:
    #     message = template.format(name=n)

    #     print()
    #     print(message)
    #     print()
    #     print()

    return valid, ids, template 