# import the module
# import tweepy
import subprocess

# # assign the values accordingly
# consumer_key = "56iEG9xVd1ToyEoAWJN9PxW1j"
# consumer_secret = "E84NQiMXKBXa7oFAHzL3aFfXY8Yr061UGJRVvXAWDMjfAXCQ40"
# access_token = "1364556305545846786-JiQPezkbhV1q3wS0UftPR0eEwB8Yjf"
# access_token_secret = "CJjf5CqK1LTqDn3kgGgt31sbodjlmsOqcQZ1ebIeEu4Uq"

# # authorization of consumer key and consumer secret
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# # set access to user's access key and access secret
# auth.set_access_token(access_token, access_token_secret)

# # calling the api
# api = tweepy.API(auth)

# # the text to be tweeted
# status = "This is a media upload.\nhttps://opensea.io/assets/0xa98771a46dcb34b34cdad5355718f8a97c8e603e/1267032129537"

# # the path of the media to be uploaded
# filename = "https://gateway.pinata.cloud/ipfs/QmZjhdfoJJy9X1UUW5bs5m4e7HpnbbzjyRNtXURnUAqDzx"

# posting the tweet
# api.update_status(status)
# subprocess.Popen("pushd ./contracts/chainlink/scripts", shell=True)
# subprocess.Popen("brownie run ./contracts/chainlink/scripts/vrf_scripts/deploy_vrf.py  --network kovan", shell=True)
# print('1 worked.')
# subprocess.Popen("brownie run ./contracts/chainlink/scripts/vrf_scripts/fund_vrf.py  --network kovan", shell=True)
# subprocess.Popen("brownie run  ./contracts/chainlink/scripts/vrf_scripts/request_randomness.py  --network kovan", shell=True)
# subprocess.Popen("brownie run  ./contracts/chainlink/scripts/vrf_scripts/read_random_number.py  --network kovan", shell=True)