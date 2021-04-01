import tweepy
import time
import os
import csv 
import random

from keys import *


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Change the Owner Name here in order to get admin access and privileges
OWNER_NAME = "RankJay1"

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
        # if '#helloworld' in mention.full_text.lower():
        #     print('found #helloworld!', flush=True)
        #     print('responding back...', flush=True)
        #     api.update_status('Hey @' + mention.user.screen_name + " thanks for mentioning me. I am currently being developed by @" + OWNER_NAME + ". Follow me @Cleopat51842118, if you haven't already.", mention.id)

        
        
        # elif '#buildcheck' in mention.full_text.lower():
        #     print('found #buildcheck!', flush=True)
        #     print('responding back...', flush=True)
        #     if mention.user.screen_name==OWNER_NAME:
        #         api.update_status('Hello Maker, @' + mention.user.screen_name + ' My build is succesfull, I am up and running!', mention.id)
        #     else:
        #         api.update_status('Hello, @' + mention.user.screen_name + ' I am sorry, but I have not detected the presence of my maker @' + OWNER_NAME + ' in this hex, unfortunately you are not authorized to check this build!', mention.id)
        
        
        
        # elif 'dm' in mention.full_text.lower():
        #     print('found DM!', flush=True)
        #     print('responding via DM...', flush=True)
        #     api.send_direct_message(mention.user.id, "Hey there! This is Cleopatra, a ChainLink paradigm, at your service.")
        #     print('responding back...', flush=True)
        #     api.update_status('Hey @' + mention.user.screen_name + ', can you check your inbox? I have just texted you.', mention.id)
        #     api.create_favorite(mention.id)

        
        
        # elif (('pricefeed' or '#pricefeed') or ('link' and ('pricefeed' or '#pricefeed'))) in mention.full_text.lower():
        #     print('found Price Feed request!', flush=True)
        #     print('responding via DM...', flush=True)
        #     # os.system('cd ./chainlink/scripts')
        #     # os.system('python chainlink/scripts/price_feed_scripts/keys.py')
        #     # os.system('cd ./chainlink/scripts/price_feed_scripts')
        #     # os.system('brownie run chainlink/scripts/price_feed_scripts/deploy_price_consumer_v3.py --network kovan')
        #     # os.system('brownie run chainlink/scripts/price_feed_scripts/read_price_feed.py --network kovan')
            
        #     cumulativePriceFeed = import_csv('./chainlink/scripts/price_feed_scripts/PriceSheet.csv')
        #     latestPriceFeed = cumulativePriceFeed[-1]
        #     DM = latestPriceFeed[0]
            
        #     api.send_direct_message(mention.user.id, "The latest price feed change of ChainLink is: " + DM)
        #     print('responding back...', flush=True)

        #     api.update_status('Hey @' + mention.user.screen_name + ', the latest price feed change of ChainLink is: ' + DM + ' wei.', mention.id)
            
        #     api.create_favorite(mention.id)

        

        # elif (('giveaway' or '#giveaway') or ('chainlink' and ('giveaway' or '#giveaway'))) in mention.full_text.lower():
        #     print('found Giveaway Thread!', flush=True)
        #     if mention.user.screen_name==OWNER_NAME:
        #         print('connecting to the giveaway thread...', flush=True)
        #         tweet = mention.full_text.lower()
        #         subHash = '#'
        #         giveawayLimit = '!'
        #         keywords = [str(x) for x in tweet.split(" ")]
        #         thread = [tweet for tweet in keywords if subHash in tweet]
        #         Alert = [tweet for tweet in keywords if giveawayLimit in tweet]
        #         retweetersScript.retweetersScraping(thread[0][1:])
        #         Validators, Identity, Template = getWinners.randomGiveaway(thread[0][1:], OWNER_NAME, int(Alert[0][1:]))

        #         winners_indx = ProcessingRandomness(int(mention.id))
        #         GIVEAWAY_DATABASE.append(thread[0][1:])
        #         lis = ''
        #         for i in range(0, len(winners_indx)):
        #             lis += str(Validators[int(winners_indx[i])]) + ', '
        #             # api.send_direct_message(Identity[i], Template.format(name=Validators[int(winners_indx[i])]))

        #         api.update_status("Hey @" + mention.user.screen_name + ",\nWinners of today's giveaway are " + lis + ".\nDMs to avail the GPR tokens have been sent to winners.", mention.id)
        #         api.create_favorite(mention.id)

        #     else:
        #         print('Authorization failed, ' + mention.user.screen_name + ' does not have the necesarry credentials to activate the giveaway.', flush=True)
        #         api.update_status('Hey @' + mention.user.screen_name + ", unfortunately you don't have the credentials to activate a giveaway. I would recommend you to join ChainLink to use this.\n P.S. I really appreciate you tagging me, thanks. Let me know if I can help you with anything else.", mention.id)
        #         api.create_favorite(mention.id)

while True:
    replyToTweets()
    n = random.randint(1, 10)
    time.sleep(n)