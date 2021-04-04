import tweepy
import time
import os
import csv 
import random
import popen

from keys import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Change the Owner Name here in order to get admin access and privileges
OWNER_NAME = "RankJay1"
# =====================================================================


# NFT Tweet Generation

def NFTTweet(userName, platform, NFTLink):
    if platform.lower()=="opensea":
        linkToNFT = "" + str(NFTLink)
    elif platform.lower()=="rarible":
        linkToNFT = "" + str(NFTLink)
    
    message = "Hello Fam!\nWe have minted yet another NFT by @" + str(userName) + ". Go check it out at " + str(platform.title()) + " with this link\n" + str(linkToNFT) 
    api.update_status(message)
    # pass



# NFT Tweet Reply

FILE_NAME = 'LastSeenId.txt'

def retrieveLastSeenId(file_name):
    f_read = open(file_name, 'r')
    lastSeenId = int(f_read.read().strip())
    f_read.close()
    return lastSeenId

def storeLastSeenId(lastSeenId, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(lastSeenId))
    f_write.close()
    return

def replyToTweets():
    print('Cleopatra is up and running...', flush=True)

    lastSeenId = retrieveLastSeenId(FILE_NAME)

    mentions = api.mentions_timeline(lastSeenId, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        lastSeenId = mention.id
        storeLastSeenId(lastSeenId, FILE_NAME)


# NFT DM Reply

def NFTDMReply(receiver):
    if 'Hi' in mention.full_text.lower():
        message = ''
        api.send_direct_message(receiver, message)


# Script Runner
