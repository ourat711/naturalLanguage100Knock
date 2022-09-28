import gzip
import json
import pprint
fileName = "jawiki-country.json.gz"
pickUp = "=="
title = "イギリス"

def wikiDataList():
  wikiDataList = []
  with gzip.open(fileName, mode='rt') as dataFile:
    for line in dataFile:
      wikiDataList.append(json.loads(line))
  return wikiDataList

def equalCount(list):
  returnList = []
  for word in list:
    for count, value in enumerate(word):
      if value != "=":
        returnList.append(word[count:-1*count].strip() + "(" + str(count-1) + ")")
        break
  return returnList

for wikiData in wikiDataList():
  print(wikiData['title'])
  dataList = wikiData['text'].splitlines()
  pickUpList = [i for i in dataList if pickUp in i] 

  if bool(pickUpList):
    pprint.pprint(equalCount(pickUpList))
