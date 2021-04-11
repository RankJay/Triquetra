#!/usr/bin/python3
from brownie import VRFConsumer
import csv

STATIC_SEED = 123

def predictionDataWriter(inputFromBot):
    with open('RandomnessSheet.csv', 'a', newline='') as deepLearningTrainer:
      trainer = csv.writer(deepLearningTrainer)
      try:
        if len(str(inputFromBot))>1 and float(inputFromBot)==True:
          trainer.writerow([inputFromBot])
        else:
          trainer.writerow([inputFromBot])
      except ValueError:
        if len(inputFromBot)>1:
          trainer.writerow([])

def main():
    vrf_contract = VRFConsumer[len(VRFConsumer) - 1]
    predictionDataWriter(vrf_contract.randomResult())
    print(vrf_contract.randomResult())
