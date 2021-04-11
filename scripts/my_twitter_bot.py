import tweepy
import time
import os
import csv 
import random
import OpenSeaFetcher
import RaribleFetcher

from keys import *
import retweetersScript
import getWinners

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Change the Owner Name here in order to get admin access and privileges
OWNER_NAME = "RankJay1"
# =====================================================================


# NFT Tweet Generation

def NFTTweet(trade):
    token_id_of_nft_parser = '#'
    asset_contract_address_of_nft_parser = '!'
    keywords = [str(x) for x in trade.split(" ")]
    token_id_of_nft = [tweet for tweet in keywords if token_id_of_nft_parser==tweet[0]]
    asset_contract_address_of_nft = [tweet for tweet in keywords if asset_contract_address_of_nft_parser==tweet[0]]
    if "opensea" in keywords:
        platform = 'opensea'
        nftName, NFTLink = OpenSeaFetcher.OpenSeaFetchingSchema(token_id_of_nft[0][1:], asset_contract_address_of_nft[0][1:])
        linkToNFT = "" + str(NFTLink)
        message = "Hello Fam!\nWe have minted yet another NFT named @" + str(nftName) + ". Go check it out at " + str(platform.title()) + " with this link\n" + str(linkToNFT) 

    elif "rarible" in keywords:
        platform = 'rarible'
        NFTLink = RaribleFetcher.RaribleFetchingSchema(token_id_of_nft[0][1:])
        linkToNFT = "" + str(NFTLink)
        message = "Hello Fam!\nWe have minted yet another NFT. Go check it out at " + str(platform.title()) + " with this link\n" + str(linkToNFT) 
    
    return message




# NFT Giving Random Giveaway

def import_csv(csvfilename):
    data = []
    with open(csvfilename, "r", encoding="utf-8", errors="ignore") as scraped:
        reader = csv.reader(scraped, delimiter=',')
        row_index = 0
        for row in reader:
            if row:
                row_index += 1
                columns = [row[0]]
                data.append(columns)
    return data

def ProcessingRandomness(Tweet_ID):
    Limit = getWinners.returnLimit()
    cumulativeRandomness = import_csv('./contracts/chainlink/scripts/RandomnessSheet.csv')
    latestRandomness = cumulativeRandomness[-1]
    ranD = int(latestRandomness[0])
    ranDcopy = int(ranD)
    quot = ranD % int(Tweet_ID)
    
    while(len(str(ranD))>len(str(int(Tweet_ID)))):
        ranD = ranD//int(Tweet_ID)
    
    picker = ranD//(10**(len(str(ranD))-1))
    j=0
    arr_idx = []
    for i in range(Limit):
        arr_idx.append(str(ranDcopy)[j:j+2])
        j+=picker
        i+=1

    return arr_idx



# NFT Tweet Reply

FILE_NAME = './scripts/LastSeenId.txt'

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
    print('Triquetra is up and running...', flush=True)

    lastSeenId = retrieveLastSeenId(FILE_NAME)

    mentions = api.mentions_timeline(lastSeenId, tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        lastSeenId = mention.id
        storeLastSeenId(lastSeenId, FILE_NAME)
        if 'publicize' in mention.full_text.lower():
            msg = NFTTweet(mention.full_text.lower())
            api.update_status(msg, mention.id)
        elif (('giveaway' or '#giveaway') or ('chainlink' and ('giveaway' or '#giveaway'))) in mention.full_text.lower():
            print('found Giveaway Thread!', flush=True)
            if mention.user.screen_name==OWNER_NAME:
                print('connecting to the giveaway thread...', flush=True)
                
                # ADD ACTIVATOR PYTHON SCRIPT
                
                tweet = mention.full_text.lower()
                subHash = '#'
                giveawayLimit = '!'
                keywords = [str(x) for x in tweet.split(" ")]
                thread = [tweet for tweet in keywords if subHash in tweet]
                Alert = [tweet for tweet in keywords if giveawayLimit in tweet]
                retweetersScript.retweetersScraping(thread[0][1:])
                Validators, Identity, Template = getWinners.randomGiveaway(thread[0][1:], OWNER_NAME, int(Alert[0][1:]))

                winners_indx = ProcessingRandomness(int(mention.id))
                GIVEAWAY_DATABASE.append(thread[0][1:])
                lis = ''
                for i in range(0, len(winners_indx)):
                    lis += str(Validators[int(winners_indx[i])]) + ', '
                    # api.send_direct_message(Identity[i], Template.format(name=Validators[int(winners_indx[i])]))

                api.update_status("Hey @" + mention.user.screen_name + ",\nWinners of today's giveaway are " + lis + ".\nDMs to avail the GPR tokens have been sent to winners.", mention.id)
                api.create_favorite(mention.id)

            else:
                print('Authorization failed, ' + mention.user.screen_name + ' does not have the necesarry credentials to activate the giveaway.', flush=True)
                api.update_status('Hey @' + mention.user.screen_name + ", unfortunately you don't have the credentials to activate a giveaway. I would recommend you to join ChainLink to use this.\n P.S. I really appreciate you tagging me, thanks. Let me know if I can help you with anything else.", mention.id)
                api.create_favorite(mention.id)



# NFT DM Reply

def NFTDMReply(receiverID, receiverName):
    if 'Hi' in mention.full_text.lower():
        message = 'Hey' + receiverName + ',\ncheck this NFT out. It is one of the latest most liked NFT present on top NFT marketplaces.\n' + 'Check it out on:'
        api.send_direct_message(receiverID, message)


# Script Runner
while True:
    replyToTweets()
    n = random.randint(1, 10)
    time.sleep(n)