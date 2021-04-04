#!/usr/bin/python3
from brownie import PriceFeed
import csv

def predictionDataWriter(inputFromBot):
    with open('D:\ChainT2\chainlink\scripts\price_feed_scripts\PriceSheet.csv', 'a', newline='') as deepLearningTrainer:
      trainer = csv.writer(deepLearningTrainer)
      try:
        if len(inputFromBot)>1 and float(inputFromBot)==True:
          trainer.writerow([inputFromBot])
        else:
          trainer.writerow([inputFromBot])
      except ValueError:
        if len(inputFromBot)>1:
          trainer.writerow([])

def main():
    price_feed_contract = PriceFeed[len(PriceFeed) - 1]
    print("Reading data from {}".format(price_feed_contract.address))
    # web3DataLoader.answer = price_feed_contract.getLatestPrice()
    gelato = price_feed_contract.getLatestPrice()
    predictionDataWriter(str(gelato))
    print(price_feed_contract.getLatestPrice())
