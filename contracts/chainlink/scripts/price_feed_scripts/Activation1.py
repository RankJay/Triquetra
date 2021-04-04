import os

os.system('pushd D:\ChainT\chainlink\scripts\price_feed_scripts')
os.system('brownie run scripts/price_feed_scripts/deploy_price_consumer_v3.py --network kovan')
os.system('brownie run scripts/price_feed_scripts/read_price_feed.py --network kovan')