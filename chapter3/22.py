# coding: utf-8
import gzip
import json
fileName = "jawiki-country.json.gz"
pickUp = "[[Category:"

def wikiDataList():
    wikiDataList = []
    with gzip.open(fileName, mode='rt') as dataFile:
        for line in dataFile:
            wikiDataList.append(json.loads(line))
    return wikiDataList

for list in wikiDataList():
    lists = list['text'].splitlines()

    pickUpList = [i.lstrip(pickUp).rstrip(']]') for i in lists if pickUp in i] 

    if bool(pickUpList):
        print(pickUpList)
