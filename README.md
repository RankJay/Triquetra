# Triqũetra

Your personal NFT Marketplace.

Add your token_id and key_access and get yourself a free tweet to publicisize your NFT on twitter.

## Pre Requisites

- Eth-Brownie
- Python 3.7
- Tweepy

## Quick Start

The entire module flow of programs have been set according to present working directory as `Triquetra/contracts/chainlink/scripts`

```
cd ./contracts/chainlink/scripts
python ../../../my_twitter_bot.py
```

## Scripts

`my_twitter_bot` : This script basiaclly is the master script to run the entire twitter bot alongside implementing its all functionalities.

`Activator` : This script is worker thread that does deployment of smart contracts to automate the process of getting VRF Random Number 

`OpenSeaFetcher` : This script basically is GET Request response handler for OpenSea backed NFTs.

`RaribleFetcher` : This script basically is GET Request response handler for Rarible backed NFTs.

## Tweet Illustrations