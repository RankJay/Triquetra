# Triqũetra

Your personal NFT Marketing Bot.

Add your token_id and asset_address and get yourself a free tweet to publicisize your NFT on twitter.

## Pre Requisites

- Eth-Brownie
- Python 3.7
- Tweepy

## Quick Start

The entire module flow of programs have been set according to present working directory as `Triquetra/contracts/chainlink/scripts`

```
cd ./contracts/chainlink/scripts
python ../../../scripts/my_twitter_bot.py
```

## Scripts

`my_twitter_bot` : This script basiaclly is the master script to run the entire twitter bot alongside implementing its all functionalities.

`Activator` : This script is worker thread that does deployment of smart contracts to automate the process of getting VRF Random Number 

`OpenSeaFetcher` : This script basically is GET Request response handler for OpenSea backed NFTs.

`RaribleFetcher` : This script basically is GET Request response handler for Rarible backed NFTs.

## Tweet Illustrations

Tweet the following in order to generate the marketing tweet

- ### **OpenSea Support** _(token_id, asset_contract_address)_
    ```
    Hey @triquet77786036,
    publicize the NFT deployed on opensea having token id #40930059826298205183487168041223830856677554863973398691462482759410010554369 and having asset address !0x495f947276749ce646f68ac8c248420045cb7b5e
    ```

- ### **Rarible Support** _(token_id)_
    ```
    Hey @triquet77786036,
    publicize the NFT deployed on rarible having token id #0xd07dc4262bcdbf85190c01c996b4c06a461d2430:0x000000000000000000000000000000000000000000000000000000000006fcc8
    ```

- ### **Sending Giveaways** _(thread_id)_
    ```
    Hey @triquet77786036, for this thread #1368350709423497217 can you announce the giveaway winners.
    ```